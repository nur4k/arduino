from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.users.views import UserView


router = DefaultRouter()
router.register('user', UserView)

urlpatterns = []

urlpatterns += router.urls