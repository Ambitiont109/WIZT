from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.exceptions import ObjectDoesNotExist
from wizt.utils import randomString
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


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','email','phone_number','password','email_verified','phone_number_verified')

    def create(self,validated_data):
        user = User.objects.create(**validated_data)
        user.username = validated_data['email']
        user.set_password(validated_data['password'])

        plan = Plan.objects.filter(is_free=True,name="Free").first()
        user.label_cnt = plan.label_count
        user.photo_cnt = plan.photo_count
        user.save()
        return user


class FaceBookLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, validators=[])
    phone_number = serializers.CharField(max_length=20, validators=[],required=False,allow_blank=True)
    class Meta:
        model = User
        fields = ('name','email','phone_number','facebook_id','email_verified','phone_number_verified','picture','target_arn','device_type')

    def create(self,validated_data):
        email = validated_data['email']
        user = None
        try:
            user = User.objects.get(email=email)
            user.facebook_id = validated_data['facebook_id']
            for key,val in validated_data.items():
                pre_val = getattr(user,key)
                if not pre_val or pre_val == '':
                    setattr(user,key,val)
        except ObjectDoesNotExist:
            # if User.objects.filter(phone_number=validated_data['phone_number']).exists():
            #     raise serializers.ValidationError({"phone_number":["user with this phone_number already exists."]})
            user = User.objects.create()
            for key,val in validated_data.items():
                setattr(user,key,val)
            if user.phone_number != '':
                user.phone_number_verified = True
            user.username = validated_data['email']
            user.set_password(randomString())

            plan = Plan.objects.filter(is_free=True,name="Free").first()
            user.label_cnt = plan.label_count
            user.photo_cnt = plan.photo_count

        user.email_verified = True
        user.target_arn = validated_data['target_arn']
        user.device_type = validated_data['device_type']
        user.save()
        return user


class GoogleLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, validators=[])
    phone_number = serializers.CharField(max_length=20, validators=[],required=False,allow_blank=True)
    class Meta:
        model = User
        fields = ('name','email','phone_number','google_id','email_verified','phone_number_verified','picture','target_arn','device_type')

    def create(self,validated_data):
        email = validated_data['email']
        user = None
        try:
            user = User.objects.get(email=email)
            user.google_id = validated_data['google_id']
            for key,val in validated_data.items():
                pre_val = getattr(user,key)
                if not pre_val or pre_val == '':
                    setattr(user,key,val)
        except ObjectDoesNotExist:
            # if User.objects.filter(phone_number=validated_data['phone_number']).exists():
            #     raise serializers.ValidationError({"phone_number":["user with this phone_number already exists."]})
            user = User.objects.create()
            for key,val in validated_data.items():
                setattr(user,key,val)
            if user.phone_number != '':
                user.phone_number_verified = True
            user.username = validated_data['email']
            user.set_password(randomString())
            
            plan = Plan.objects.filter(is_free=True,name="Free").first()
            user.label_cnt = plan.label_count
            user.photo_cnt = plan.photo_count

        user.target_arn = validated_data['target_arn']
        user.device_type = validated_data['device_type']

        user.email_verified = True
        user.save()
        return user


class PasswordNewSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(max_length=50)
        
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
    # images = ImageSerializer(many=True, read_only=True, source='image_set')
    images = serializers.SerializerMethodField()    # this fields always read only field
    class Meta:
        model = Label
        fields = '__all__'

    def get_images(self, instance):        
        images = instance.image_set.all().order_by('-created_at')
        return ImageSerializer(images, many=True).data


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
    # email = serializers.EmailField(required=False,default=None)
    tokenId = serializers.CharField(max_length = 50,required=False,default=None)
    plan = serializers.PrimaryKeyRelatedField(queryset=Plan.objects.all())


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()
    name = serializers.CharField()


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'
