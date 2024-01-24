from django.contrib import admin

from apps.backoffice.models import GIS, Driver

admin.site.register((GIS, Driver))
