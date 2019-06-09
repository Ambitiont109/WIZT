from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Sum, Q
from backend.models import *
from .serializers import *
from backend.serializers import PlanSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,action
from rest_framework.authtoken.models import Token
from rest_framework import viewsets,status,pagination
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from wizt.utils import send_broadcast_notification
from rest_framework.exceptions import MethodNotAllowed,NotFound
import datetime
# Create your views here.


@api_view(['POST'])
def login(request):
    if request.method != 'POST':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.validated_data)
        email = serializer.validated_data['email']
        pwd = serializer.validated_data['password']
        try:
        	user = User.objects.get(email=email)
        	if user.check_password(pwd) and user.is_superuser:
        		token = Token.objects.get_or_create(user=user)
        		return Response(token[0].key,status=status.HTTP_200_OK)
        	else:
        		return Response("email or password invalid",status=status.HTTP_400_BAD_REQUEST)	
        except User.DoesNotExist:
        	return Response("email or password invalid",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser))
def delete_user_friend(request,pk,friend_pk):
    try:
        user = User.objects.get(pk=pk)
        friend = User.objects.get(pk=friend_pk)
        Friend.objects.filter(Q(from_user = user)|Q(to_user= user)).filter(Q(from_user=friend)|Q(to_user=friend)).delete()
        return Response("",status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise NotFound()


@api_view(['DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser))
def delete_user_label(request,pk,label_pk):
    try:
        user = User.objects.get(pk=pk)
        Label.objects.filter(user = user,pk=label_pk).delete()
        return Response("",status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise NotFound()


@api_view(['DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser))
def delete_user_floorplan(request,pk,floorplan_pk):
    try:
        user = User.objects.get(pk=pk)
        FloorPlan.objects.filter(user = user,pk=floorplan_pk).delete()
        return Response("",status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise NotFound()


def get_user_data_monthly():
    now = datetime.datetime.now()
    qs = (User.objects.all()
        .extra(select={'month': "EXTRACT(month FROM created_at)",'year': "EXTRACT(year FROM created_at)",})
        .values('month', 'year')
        .annotate(count_items=Count('created_at'))).filter(created_at__year=now.year)
    qs = qs.order_by('month')
    return qs


def get_earning_data_mothly():
    now = datetime.datetime.now()
    qs = (Transaction.objects.all()
        .extra(select={'month': "EXTRACT(month FROM created_at)",'year': "EXTRACT(year FROM created_at)",})
        .values('month', 'year')
        .annotate(sum=Sum('pay_amount'))).filter(created_at__year=now.year)
    qs = qs.order_by('month')
    return qs


@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser))
def dashboard(request):
    # users = get_user_data_monthly()
    users = User.objects.count()
    earnings = get_earning_data_mothly()
    label_counts = Label.objects.count()
    image_counts = Image.objects.count()
    statistics = {
        'users':users,
        'earnings':earnings,
        'label_counts':label_counts,
        'image_counts':image_counts
    }

    return Response(statistics,status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,IsAdminUser))
def updatePassword(request):
    serializer = UpdatePasswordSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    current_password = serializer.data['current_password']
    new_password = serializer.data['new_password']
    user = request.user
    if not user.check_password(current_password):
        return Response('current password is incorrect ',status=status.HTTP_401_UNAUTHORIZED)
    user.set_password(new_password)
    user.save()
    serializer = UserSerializerForRead(instance=user)
    return Response(serializer.data,status=status.HTTP_200_OK)

    
@api_view(['POST','GET'])
@permission_classes((IsAuthenticated,IsAdminUser))
def updateProfile(request):
    if request.method == 'POST':
        serializer = UpdateProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.data['name']
        email = serializer.data['email']
        user = request.user
        user.name = name
        user.username = email
        user.email = email
        user.save()
        serializer = UserSerializerForRead(instance=user)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method == 'GET':
        user = request.user
        serializer = UpdateProfileSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)

    


class UsersViewSet(viewsets.ModelViewSet,):
    permission_classes = (IsAuthenticated,IsAdminUser)
    serializer_class = UserSerializer
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        return User.objects.all().exclude(is_superuser=True)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all().exclude(is_superuser=True)
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


    @action(methods=['POST'], detail=False,url_path='pagination')  # set pagination size
    def set_pagination(self,request):
        try:
            print(request.data)
            pagination_size = request.data['pagination_size']
            self.pagination_class.page_size = pagination_size
        except Exception as e:
            return Response('{"pagination_size":"Require Pagination Size"}',status=status.HTTP_400_BAD_REQUEST)
        return Response("success",status=status.HTTP_200_OK)



class LabelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,IsAdminUser)
    serializer_class = LabelSerializer
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        return Label.objects.order_by('-updated_at').all()

    @action(methods=['POST'], detail=False,url_path='pagination')  # set pagination size
    def set_pagination(self,request):        
        try:
            print(request.data)
            pagination_size = request.data['pagination_size']
            self.pagination_class.page_size = pagination_size
        except Exception as e:
            return Response('{"pagination_size":"Require Pagination Size"}',status=status.HTTP_400_BAD_REQUEST)
        return Response("success",status=status.HTTP_200_OK)


class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,IsAdminUser)
    serializer_class = TransactionSerializer
    pagination_class = pagination.PageNumberPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return TransactionSerializer
        elif self.action == 'retrieve':
            return TransactionDetailSerializer
        else:
            return TransactionSerializer
    def get_queryset(self):
        return Transaction.objects.all()

    @action(methods=['POST'], detail=False,url_path='pagination')  # set pagination size
    def set_pagination(self,request):
        try:
            print(request.data)
            pagination_size = request.data['pagination_size']
            self.pagination_class.page_size = pagination_size
        except Exception as e:
            return Response('{"pagination_size":"Require Pagination Size"}',status=status.HTTP_400_BAD_REQUEST)
        return Response("success",status=status.HTTP_200_OK)


class PlanViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,IsAdminUser)
    serializer_class = PlanSerializer

    def get_queryset(self):
        return Plan.objects.all()


class NotificaionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,IsAdminUser)
    serializer_class = NotificationWriteSerializer
    pagination_class = pagination.PageNumberPagination

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return NotificationReadSerializer
        else:
            return NotificationWriteSerializer

    def get_queryset(self):
        # self.request.data['send_by'] = self.request.user.id
        return Notification.objects.filter(message_type=0).order_by('-created_at') # get broad casted notifications and received notifications
   
    def create(self, request, *args, **kwargs):
        request.data['send_by'] = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        notification = serializer.save()
        topic_arn = "arn:aws:sns:ap-southeast-1:417479686763:wizt"
        send_broadcast_notification(topic_arn,"admin",notification.message)

        headers = self.get_success_headers(serializer.data)
        serializer = NotificationReadSerializer(instance = notification)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    @action(methods=['POST'], detail=False,url_path='pagination')  # set pagination size
    def set_pagination(self,request):
        try:
            print(request.data)
            pagination_size = request.data['pagination_size']
            self.pagination_class.page_size = pagination_size
        except Exception as e:
            return Response('{"pagination_size":"Require Pagination Size"}',status=status.HTTP_400_BAD_REQUEST)
        return Response("success",status=status.HTTP_200_OK)