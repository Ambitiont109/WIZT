from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    email_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, unique=True, null=True)
    phone_number_verified = models.BooleanField(default=False)
    picture = models.URLField(max_length=100, null=True)
    total_label_count = models.IntegerField(default=0)
    label_in_use = models.IntegerField(default=100)
    friends_count = models.IntegerField(default=0)
    friends = models.ManyToManyField('User', through='Friend', symmetrical=False, related_name='friends+')    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "users"
        unique_together = (('id', 'email', 'phone_number'),)


class Label(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="labels", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    tags = models.CharField(max_length=200)
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
    mobile = models.CharField(max_length=20)
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
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    snapshot = models.URLField()
    is_image_type = models.BooleanField(default=False)
    shape_image = models.URLField()
    shapes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "floor_plans"


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


class Plan(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.IntegerField()
    photo_count = models.IntegerField()
    label_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "plans"
