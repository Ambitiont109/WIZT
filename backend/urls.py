from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from backend import views
from backend.views import *
from backend import stripe


router = DefaultRouter()
router.register('labels', LabelViewSet, basename='label')
router.register('users/friends/request', FriendViewSet, basename='friend')
router.register('users', UserViewSet, basename='user')
router.register('notifications',NotificaionViewSet,basename='notification')
router.register('share/labels',ShareLabelViewSet,basename='sharelabel')
router.register('plans',PlanViewSet,basename='plan')
router.register('floorplans',FloorPlanViewSet,basename='floorplan')

urlpatterns = [
    # Authentication
    path('login', views.login),
    path('register/',views.register),
    path('login/facebook/',views.login_facebook),
    path('login/google/',views.login_google),
    path('password/new/',views.password_new),
    path('logout', views.logout),
    path('users/friends/', FriendsList.as_view({'get': 'list'})),
    path('profile/',show_profile),
    
    path('address/',AddressViewSet.as_view()),
    path('stripe/getCustomer/',stripe.getCustomer),
    path('stripe/createCustomer/',stripe.createCustomer),
    path('stripe/addCardToCustomer/',stripe.addCardToCustomer),
    path('stripe/createCustomerKey/',stripe.createCustomerKey),
    path('stripe/doPayment/',stripe.doPayment),
    path('stripe/doSubscription/',stripe.doSubscription),
    path('stripe/deleteSubscription/',stripe.deleteSubscription),
    path('', include(router.urls)),

]
