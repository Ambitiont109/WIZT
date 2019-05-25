from django.shortcuts import render, get_object_or_404
from backend.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
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


class UsersViewSet(viewsets.ModelViewSet,):
    permission_classes = (IsAuthenticated,IsAdminUser)
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


class LabelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,IsAdminUser)
    serializer_class = LabelSerializer

    def get_queryset(self):
        return Label.objects.order_by('-updated_at').all()


class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,IsAdminUser)
    serializer_class = Transaction

    def get_serializer_class(self):
        if self.action == 'list':
            return TransactionSerializer
        elif self.action == 'retrieve':
            return TransactionDetailSerializer
        else:
            return TransactionSerializer
    def get_queryset(self):
        return Transaction.objects.all()

