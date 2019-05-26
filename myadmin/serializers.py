from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from backend.models import *
from backend.serializers import LabelSerializer,ImageSerializer,PlanSerializer,FloorPlanReadSerializer

class LoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField(max_length=100)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password','last_login','is_superuser','is_staff','is_active','date_joined','groups','user_permissions','friends','subscribed_customer_id','subscribed_token_id','subscription_id')

class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Transaction
        exclude = ('plan',)


class TransactionDetailSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()
    user = UserSerializer()
    class Meta:
        model = Transaction
        fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer):
    friends = UserSerializer(many=True,read_only=True)
    labels = LabelSerializer(many=True,read_only=True)
    transactions = TransactionSerializer(many=True,read_only=True)
    floorplans = FloorPlanReadSerializer(many=True,read_only=True,source='floor_plans')
    class Meta:
        model = User
        exclude = ('password','last_login','is_superuser','is_staff','is_active','date_joined','groups','user_permissions')

class LabelSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True, source='image_set')
    class Meta:
        model = Label
        fields = '__all__'


