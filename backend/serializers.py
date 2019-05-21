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


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'


class NotificationSerizlier(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class ShareLabelSerializer(serializers.ModelSerializer):
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

