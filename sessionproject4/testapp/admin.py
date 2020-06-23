from django.contrib import admin
from testapp.models import HomeModel

# Register your models here.
class HomeModelAdmin(admin.ModelAdmin):
    list_display=['coursename','quantity']

admin.site.register(HomeModel,HomeModelAdmin)
