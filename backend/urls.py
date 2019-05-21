from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from backend import views
from backend.views import *

router = DefaultRouter()
router.register('labels', LabelViewSet, basename='label')
router.register('users/friends/request', FriendViewSet, basename='friend')
router.register('users', UserViewSet, basename='user')
router.register('notifications',NotificaionViewSet,basename='notification')
router.register('share/labels',ShareLabelViewSet,basename='sharelabel')
router.register('plans',PlanViewSet,basename='plan')

urlpatterns = [
    # Authentication
    path('login', views.login),
    path('logout', views.logout),
    path('users/friends/', FriendsList.as_view({'get': 'list'})),
    path('profile/',show_profile),
    path('address/',AddressViewSet.as_view()),
    path('', include(router.urls)),

]
