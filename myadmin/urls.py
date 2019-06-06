from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
# router.register('labels', LabelViewSet, basename='label')
# router.register('users/friends/request', FriendViewSet, basename='friend')
# router.register('users', UserViewSet, basename='user')
# router.register('notifications',NotificaionViewSet,basename='notification')
# router.register('share/labels',ShareLabelViewSet,basename='sharelabel')
router.register('plans',PlanViewSet,basename='plan')
router.register('notifications',NotificaionViewSet,basename='notifications')

urlpatterns = [
    # Authentication
    path('login/', login),
    path('users/<int:pk>/',UsersViewSet.as_view({'get':'retrieve'})),
    path('users/',UsersViewSet.as_view({'get':'list'})),
    path('users/pagination/',UsersViewSet.as_view({'post':'set_pagination'})),
    path('labels/',LabelViewSet.as_view({'get':'list'})),
    path('labels/<int:pk>/',LabelViewSet.as_view({'get':'retrieve'})),
    path('labels/pagination/',LabelViewSet.as_view({'post':'set_pagination'})),
    path('transactions/',TransactionViewSet.as_view({'get':'list'})),
    path('transactions/pagination/',TransactionViewSet.as_view({'post':'set_pagination'})),
    path('transactions/<int:pk>/',TransactionViewSet.as_view({'get':'retrieve'})),
    path('dashboard/',dashboard),
    path('account/password/',updatePassword),
    path('account/',updateProfile),

    # path('logout', views.logout),
    # path('users/friends/', FriendsList.as_view({'get': 'list'})),
    # path('profile/',show_profile),
    # path('address/',AddressViewSet.as_view()),
    path('', include(router.urls)),

]
