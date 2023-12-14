from django.contrib import admin

from apps.main_app.models import Item, Driver


admin.site.register((Item, Driver))
