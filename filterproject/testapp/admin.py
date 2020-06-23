from django.contrib import admin
from testapp.models import Filtermodel
class FiltermodelAdmin(admin.ModelAdmin):
    list_display=['name','subject','dept','date']
admin.site.register(Filtermodel,FiltermodelAdmin)
