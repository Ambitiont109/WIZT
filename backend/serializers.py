from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import *


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, validators=[UniqueValidator(queryset=User.objects.all())])
    phone_number = serializers.CharField(max_length=50, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('name', 'email', 'email_verified', 'phone_number', 'phone_number_verified', 'picture', 'username')


class UserSerializerForFriend(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'phone_number', 'picture', 'username', 'id')


class UserSerializerForRead(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'phone_number', 'picture', 'username', 'id')





class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        extra_kwargs = {'label': {'write_only': True}}
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True, source='image_set')

    class Meta:
        model = Label
        fields = '__all__'


class FriendReadSerializer(serializers.ModelSerializer):
    from_user = UserSerializerForFriend()
    to_user = UserSerializerForFriend()
    class Meta:
        model = Friend
        fields = '__all__'


class FriendWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'        

class NotificationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'



class NotificationReadSerializer(serializers.ModelSerializer):
    send_by = UserSerializerForRead()
    send_to = UserSerializerForRead()
    class Meta:
        model = Notification
        fields = '__all__'


class ShareLabelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareLabel
        fields = '__all__'


class ShareLabelReadSerializer(serializers.ModelSerializer):
    label = LabelSerializer()
    share_by = UserSerializerForRead()
    share_to = UserSerializerForRead()
    class Meta:
        model = ShareLabel
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class FloorPlanWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorPlan
        fields = '__all__'


class FloorPlanReadSerializer(serializers.ModelSerializer):
    user = UserSerializerForRead()
    class Meta:
        model = FloorPlan
        fields = '__all__'


class SubscribeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False,default=None)
    tokenId = serializers.CharField(max_length = 50,required=False,default=None)
    plan = serializers.PrimaryKeyRelatedField(queryset=Plan.objects.all())