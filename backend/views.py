from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.views import View
from django.db.models import Q
from rest_framework import viewsets,mixins
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import MethodNotAllowed,NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,action,parser_classes
from rest_framework import permissions,parsers
from rest_framework.permissions import IsAuthenticated
from botocore.exceptions import ClientError

from django.http import Http404
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from myadmin.serializers import UserSerializer as OtherUserSerializer
from .models import *
import boto3


# @api_view(['POST'])
# def login(request):
#     if request.method != 'POST':
#         return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#     access_token = request.headers.get("Authorization")
#     client = boto3.client('cognito-idp', region_name='ap-southeast-1')
#     try:
#             # HTTP HEAD request
#         user_dic = client.get_user(AccessToken=access_token.replace('Bearer ', ''))
#     except ClientError as e:
#         if e.response['Error']['Code'] == 'EntityAlreadyExists':
#             return Response("User already exists",status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response("Unexpected error: %s" % e,status=status.HTTP_400_BAD_REQUEST)
#     serializer_data = {}

#     for item in user_dic['UserAttributes']:
#         serializer_data[item['Name']] = item['Value']

#     serializer_data['username'] = serializer_data['email']
#     serializer = UserSerializer(data=serializer_data)

#     if serializer.is_valid():
#         user = serializer.save()
#     else:
#         user = User.objects.get(email=serializer_data['email'])

#     token = Token.objects.get_or_create(user=user)
#     return Response(token[0].key,status=status.HTTP_200_OK)
def create_notification(send_by,send_to,message,message_type):
    notification = Notification.objects.create(send_by=send_by,send_to=send_to,message_type=message_type,message=message)
    notification.save()


@api_view(['POST'])
def file_upload(request):
    print(request.data)
    print(request.FILES)
    file_serializer =FileSerializer(data=request.data)
    file_serializer.is_valid(raise_exception=True)
    print(request.data)
    # print(request.data['file'])
    return Response(file_serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
def login(request):
    try:
        email = request.data['email']
        pwd = request.data['password']
    except Exception as e:
        return Response('Must include "email" and "password"',status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(email=email)    
        if not user.check_password(pwd):
            return Response('email or password is invalid',status=status.HTTP_400_BAD_REQUEST)
        token = Token.objects.get_or_create(user=user)
        return Response(token[0].key,status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response('email or password is invalid',status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        serializer = UserSerializer(instance=user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_facebook(request):
    serializer = FaceBookLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.get_or_create(user=user)
        return Response(token[0].key,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_google(request):
    serializer = GoogleLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.get_or_create(user=user)
        return Response(token[0].key,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def password_new(request):
    serializer = PasswordNewSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        pwd = serializer.validated_data['password']
        try:
            user = User.objects.get(email=email)    
            user.set_password(pwd)
            user.save()
            serializer = UserSerializer(instance=user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response('email is not exists',status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def logout(request):
    token = Token.objects.get(user=request.user)
    token.delete()
    return Response("",status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().exclude(is_superuser=True)
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LabelViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LabelSerializer

    def get_queryset(self):
        self.request.data['user'] = self.request.user.id
        return Label.objects.filter(user=self.request.user)

    def update(self,request,pk):
        try:
            label = Label.objects.get(pk=pk)
            if label.user != request.user:
                share_label = ShareLabel.objects.filter(label=label,share_to=request.user).first()
                print(share_label)
                if share_label == None or share_label.edit_permission == False:
                    raise MethodNotAllowed(request.method)
        except Label.DoesNotExist:
            raise NotFound()
        serializer = LabelSerializer(instance=label, data=request.data,partial=True)
        print(serializer.initial_data)
        serializer.is_valid(raise_exception=True)
        for image in label.image_set.all():
            image.delete()
        images = request.data['images']
        for image in images:
            record = Image(label=label, url=image['url'], thumbnail=image['thumbnail'], is_cover=image['is_cover'])
            record.save()
        label = serializer.save()
        serializer = LabelSerializer(label)
        return Response(serializer.data)

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
        user = self.request.user
        if is_friend == 'true':
            friends = Friend.objects.filter(Q(from_user=user)|Q(to_user=user),status=True).all()
            friend_list = []
            for friend in friends:
                if(friend.to_user == user):
                    friend_list.append(friend.from_user.id)
                else:
                    friend_list.append(friend.to_user.id)
            return User.objects.filter(pk__in=friend_list).exclude(is_superuser=True)
        else:
            query = self.request.GET.get('query', '')
            friends = user.friends.all()
            unfriend_list = [user.id for user in friends]
            unfriend_list.append(user.id)
            return User.objects.exclude(pk__in=unfriend_list).filter(
                Q(username__contains=query) | Q(name__contains=query)).exclude(is_superuser=True)


class FriendViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = FriendWriteSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve' or self.action == 'update':
            self.request.data['to_user'] = self.request.user.id
            return FriendReadSerializer
        else:
            return FriendWriteSerializer

    def get_queryset(self):
        # return Friend.objects.all()      
        if self.action == 'list':  
            return Friend.objects.filter(to_user=self.request.user,status=False)
        else:
            return Friend.objects.all()

    def update(self, request, *args, **kwargs):
        response = super().update(request,*args,**kwargs)
        friend = self.get_object()
        if friend.status == True:
            create_notification(friend.from_user,friend.to_user,"Fried Request Has Been Accepted",1)
        return response

    def destroy(self, request, *args, **kwargs):
        friend = self.get_object()
        response = super().destroy(request,*args,**kwargs)
        create_notification(friend.from_user,friend.to_user,"Fried Request Has Been Deleted",1)
        return response

    def create(self, request):
        request.data['from_user'] = request.user.id
        if self.request.data.get('status', None) is None:
            self.request.data['status'] = False
        serializer = FriendWriteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        friend = serializer.save()
        create_notification(friend.from_user,friend.to_user,"Fried Request Has Been Sent",1)
        serializer = FriendReadSerializer(instance=friend)
        return Response(serializer.data)


class NotificaionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = NotificationWriteSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return NotificationReadSerializer
        else:
            return NotificationWriteSerializer

    def get_queryset(self):
        # self.request.data['send_by'] = self.request.user.id
        return Notification.objects.filter(Q(send_to = self.request.user)|Q(message_type=0)) # get broad casted notifications and received notifications
   
    def create(self, request, *args, **kwargs):
        request.data['send_by'] = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        notification = serializer.save()
        headers = self.get_success_headers(serializer.data)
        serializer = NotificationReadSerializer(instance = notification)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['delete'], detail=False,url_path='clear')  # delete_all_notifications
    def clear(self,request):
        Notification.objects.filter(Q(send_to = self.request.user)).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShareLabelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ShareLabelWriteSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ShareLabelReadSerializer
        else:
            return ShareLabelWriteSerializer

    def get_queryset(self):
        self.request.data['share_by'] = self.request.user.id
        return ShareLabel.objects.all()

    def destroy(self, request, *args, **kwargs):
        share_label = self.get_object()
        response = super().destroy(request,*args,**kwargs)
        create_notification(share_label.share_by,share_label.share_to,"Label has been shared to %s " % (share_label.share_to.name,),1)

    def list(self,request, *args, **kwargs):
        me = self.request.GET.get('me','true')
        if me == 'true':
            queryset = ShareLabel.objects.filter(share_to=self.request.user.id)
        else:
            queryset = ShareLabel.objects.filter(share_by=self.request.user.id)

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
        share_label = serializer.save()
        create_notification(share_label.share_by,share_label.share_to,"Label has been shared to %s" % (share_label.share_to.name,),1)
        headers = self.get_success_headers(serializer.data)
        serializer = ShareLabelReadSerializer(instance = share_label)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PlanViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlanSerializer

    def get_queryset(self):
        return Plan.objects.all()


@api_view(['GET','PATCH'])
@permission_classes((permissions.IsAuthenticated,))
def show_profile(request):
    instance = request.user
    if request.method == 'GET':
        serializer = OtherUserSerializer(instance)
        return Response(serializer.data)
    if request.method == 'PATCH':
        pic_url = request.data.get('picture',None)
        if(pic_url):
            request.user.picture = pic_url  
            request.user.save()      
            return Response('',status=status.HTTP_200_OK)
        else:
            return Response('',status=status.HTTP_400_BAD_REQUEST)


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


class FloorPlanViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = FloorPlanWriteSerializer
    pagination_class = None
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return FloorPlanReadSerializer
        else:
            return FloorPlanWriteSerializer

    def get_queryset(self):
        self.request.data['user'] = self.request.user.id
        return FloorPlan.objects.filter(user=self.request.user.id).order_by('-updated_at')

    def create(self,request, *args, **kwargs):
        request.data['user'] = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        share_label = serializer.save()
        headers = self.get_success_headers(serializer.data)
        serializer = FloorPlanReadSerializer(instance = share_label)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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
