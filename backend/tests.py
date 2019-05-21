from django.test import TestCase
from .models import User


class ModelTestCase(TestCase):
    def setUp(self) -> None:
        self.user_name = "Polaris"
        self.user = User(name=self.user_name)

    def test_model_can_create_a_user(self):
        old_count = User.objects.count()
        self.user.save()
        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)
