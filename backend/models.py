from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    email_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=True,blank=True)
    phone_number_verified = models.BooleanField(default=False)
    target_arn = models.CharField(max_length=100)
    device_type = models.CharField(max_length=50)
    picture = models.URLField(max_length=100, null=True,blank=True)
    total_label_count = models.IntegerField(default=0)

    label_in_use = models.IntegerField(default=0)
    photo_in_use = models.IntegerField(default = 0)
    label_cnt = models.IntegerField(default = 100)
    photo_cnt = models.IntegerField(default = 20)
    # friends_count = models.IntegerField(default=0)
    friends = models.ManyToManyField('User', through='Friend', symmetrical=False, related_name='friends+')
    #subscription part
    subscribed_email = models.EmailField(blank=True)
    subscribed_customer_id = models.CharField(max_length=50, null=True)
    subscribed_token_id = models.CharField(max_length=100,blank=True)   # customer source id
    subscribed_plan = models.ForeignKey('Plan',related_name='users',on_delete=models.CASCADE,null=True)
    subscription_id = models.CharField(max_length = 100,null=True)
    calling_date = models.DateTimeField(null=True)  # date that the label and photo count is updated
    #auth_part
    facebook_id = models.CharField(max_length = 100, blank=True,null=True)
    google_id = models.CharField(max_length=100,blank=True,null=True)
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def friends_count(self):
        return Friend.objects.filter(Q(from_user=self)|Q(to_user=self),status=True).count()
        
    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "users"
        unique_together = (('id', 'email', 'phone_number'),)


class Label(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="labels", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100,blank=True,null=True)
    tags = models.CharField(max_length=200)
    floor_plan = models.OneToOneField('FloorPlan',on_delete=models.SET_NULL,null=True)
    ar_mark_image = models.CharField(max_length=150,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "labels"
        indexes = [
            models.Index(fields=['user']),
        ]

    def __str__(self):
        return "{}".format(self.name)


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    is_cover = models.BooleanField()
    url = models.URLField(max_length=150)
    thumbnail = models.URLField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "images"
        indexes = [
            models.Index(fields=['label']),
        ]


class Friend(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name='from_users')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name='to_users')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "friends"
        unique_together = ('to_user', 'from_user')


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message_type = models.IntegerField()    # 0: broad cast , 1: Individual Notification.
    send_by = models.ForeignKey(User, related_name='sended_notifications', on_delete=models.CASCADE, blank=False)
    send_to = models.ForeignKey(User, related_name='received_notifications', on_delete=models.CASCADE, blank=False)
    message = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "notifications"


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    country = models.CharField(max_length=30)
    # mobile = models.CharField(max_length=20)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    shipping_address = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    zip_code = models.IntegerField()

    class Meta:
        db_table = "addresses"


# class Subscription(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     plan = models.ForeignKey('plans', related_name='+', editable=False, on_delete=models.SET_NULL)
#     payout = models.IntegerField()
#     expire_date = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = "subscriptions"


class FloorPlan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name='floor_plans', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tags = models.CharField(max_length=300)
    thumbnail = models.URLField()
    image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "floor_plans"
        indexes = [
            models.Index(fields=['-updated_at',])
        ]


class ShareLabel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.ForeignKey(Label, related_name='+', on_delete=models.CASCADE)
    share_by = models.ForeignKey(User, related_name='shared_labels_by_me', on_delete=models.CASCADE)
    share_to = models.ForeignKey(User, related_name='shared_labels_to_me', on_delete=models.CASCADE)

    edit_permission = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "share_labels"
        unique_together = ('label', 'share_by','share_to')

class Plan(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.CharField(max_length=100)   # represent the Product Id of the Stripe.
    # icon = models.CharField(max_length=100)
    icon = models.ImageField()
    price = models.FloatField()
    currency = models.CharField(max_length=10,default='USD')
    name = models.CharField(max_length=50)
    sub_name = models.CharField(max_length=100,default='sub_name')
    photo_count = models.IntegerField()
    label_count = models.IntegerField()
    description = models.TextField(default='description')
    is_free = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "plans"
        
class SubscribeTransaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    subscribe_email = models.EmailField()
    subscribed_token_id = models.CharField(max_length=100)
    subscription_id = models.CharField(max_length = 100)
    plan_name = models.CharField(max_length=100)
    plan_price = models.FloatField(null=True)
    plan_product_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    pay_amount = models.FloatField(blank=False,null=False)
    currency = models.CharField(max_length=50)
    name = models.CharField(max_length = 100)
    mobile_number = models.CharField(max_length = 100)
    shipping_address = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zip_code = models.CharField(max_length = 100)
    token_id = models.CharField(max_length = 100)
    ip_address = models.CharField(max_length = 100)
    payment_status = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Train(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    is_trained =  models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TrainImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    url = models.URLField(max_length=150)
    thumbnail = models.URLField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "train_images"
        indexes = [
            models.Index(fields=['train']),
        ]


class TrainModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)