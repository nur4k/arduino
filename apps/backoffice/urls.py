from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.backoffice.views import DriverView, GisView, GpsDataView

router = DefaultRouter()
router.register("gis", GisView)
router.register("driver", DriverView)

urlpatterns = [
    path("location/", GpsDataView.as_view()),
]

urlpatterns += router.urls
