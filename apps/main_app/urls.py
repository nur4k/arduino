from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.main_app.views import ItemView, DriverView, handle_data


router = DefaultRouter()
router.register('item', ItemView)
router.register('driver', DriverView)

urlpatterns = [
    path("handle_data/", handle_data),
]

urlpatterns += router.urls
