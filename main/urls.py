from django.db import router
from django.urls import path, include
from . import views
from rest_framework import routers
from .api import AuthViewSet, InviteCodeViewSet


router = routers.DefaultRouter()
router.register('apiAuth', AuthViewSet, 'auth')
router.register('apiInviteCode', InviteCodeViewSet, 'invitecode')


urlpatterns = [
    path('', views.welcome),
    path('authentication/user/<str:userid>', views.auth),
    path('profile/user/<str:userid>', views.userpage),
    path('', include(router.urls)),
    path('api/<str:phone>', InviteCodeViewSet.as_view({'get':'phones'})),
    path('api/<str:phone>/<str:code>', InviteCodeViewSet.as_view({'post':'newuser'})),
]