from django.contrib.auth.models import User, Group
from django.views import View
from django.db.models import Q
from rest_framework import viewsets,mixins
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,action
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from botocore.exceptions import ClientError
from django.http import Http404
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *
import boto3


@api_view(['POST'])
def login(request):
    if request.method != 'POST':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    access_token = request.headers.get("Authorization")
    client = boto3.client('cognito-idp', region_name='ap-southeast-1')
    user_dic = client.get_user(AccessToken=access_token.replace('Bearer ', ''))
    serializer_data = {}

    for item in user_dic['UserAttributes']:
        serializer_data[item['Name']] = item['Value']

    serializer_data['name'] = serializer_data['email']
    serializer_data['username'] = serializer_data['email']
    serializer = UserSerializer(data=serializer_data)

    if serializer.is_valid():
        user = serializer.save()
    else:
        user = User.objects.get(email=user_dic['Username'])

    token = Token.objects.get_or_create(user=user)

    return Response(token[0].key)


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def logout(request):
    pass


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LabelViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LabelSerializer

    def get_queryset(self):
        self.request.data['user'] = self.request.user.id
        return Label.objects.filter(user=self.request.user)

    def create(self, request):
        request.data['user'] = request.user.id
        serializer = LabelSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        label = serializer.save()

        images = request.data['images']
        for image in images:
            record = Image(label=label, url=image['url'], thumbnail=image['thumbnail'], is_cover=image['is_cover'])
            record.save()
        serializer = LabelSerializer(label)

        return Response(serializer.data)


class FriendsList(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializerForFriend

    def get_queryset(self):
        self.request.data['user'] = self.request.user.id
        is_friend = self.request.GET.get('is_friend', 'true')
        if is_friend == 'true':
            return self.request.user.friends.all()
        else:
            query = self.request.GET.get('query', '')
            user = self.request.user
            friends = user.friends.all()
            return User.objects.exclude(pk__in=[user.id for user in friends]).filter(
                Q(username__contains=query) | Q(name__contains=query))


class FriendViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = FriendSerializer

    def get_queryset(self):
        # return Friend.objects.all()
        self.request.data['from_user'] = self.request.user.id
        return Friend.objects.filter(from_user=self.request.user)

    def create(self, request):
        request.data['from_user'] = request.user.id
        if self.request.data.get('status', None) is None:
            self.request.data['status'] = False
        serializer = FriendSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        friend = serializer.save()
        return Response(serializer.data)


class NotificaionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = NotificationSerizlier

    def get_queryset(self):
        # self.request.data['send_by'] = self.request.user.id
        return Notification.objects.filter(Q(send_to = self.request.user)|Q(message_type=0)) # get broad casted notifications and received notifications

    def create(self, request, *args, **kwargs):
        request.data['send_by'] = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['delete'], detail=False,url_path='clear')
    def clear(self,request):
        Notification.objects.filter(Q(send_to = self.request.user)).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShareLabelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ShareLabelSerializer

    def get_queryset(self):
        self.request.data['share_by'] = self.request.user.id
        return ShareLabel.objects.all()

    def list(self,request, *args, **kwargs):
        me = self.request.GET.get('me','true')
        if me == 'true' :
            queryset = ShareLabel.objects.filter(share_by=self.request.user.id)
        else:
            queryset = ShareLabel.objects.filter(share_to=self.request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self,request, *args, **kwargs):
        request.data['share_by'] = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PlanViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlanSerializer

    def get_queryset(self):
        return Plan.objects.all()


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def show_profile(request):
    instance = request.user
    serializer = UserSerializer(instance)
    return Response(serializer.data)


class AddressViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        try:
            instance = request.user.address
            serializer = AddressSerializer(instance)
            return Response(serializer.data)
        except Address.DoesNotExist:
            raise Http404


    def post(self,request):
        request.data['user']=request.user.id
        serializer = AddressSerializer(data = request.data)
        if serializer.is_valid():
            address = serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):      
        request.data['user']=request.user.id
        instance = request.user.address
        serializer = AddressSerializer(instance = instance,data=request.data,partial=False)
        if serializer.is_valid():
            address = serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def subscribe(self, request):
        pass


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['GET', 'POST'])
def test(request):
    client = boto3.client('cognito-idp', region_name='ap-southeast-1')
    try:
        response = client.admin_get_user(UserPoolId='ap-southeast-1_FG9cOimAA', Username='fantastic12249019@gmail.com')
    except ClientError:
        print("AWS Client Error")

    return Response(response)


@api_view(['GET', 'POST'])
def test1(request):
    access_token = request.headers.get("Authorization")
    client = boto3.client('cognito-idp', region_name='ap-southeast-1')
    response = client.get_user(AccessToken=access_token.replace('Bearer ', ''))

    return Response(response)