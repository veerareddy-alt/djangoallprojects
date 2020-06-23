from django.contrib import admin
from testapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['srollno','sname','sdept']

admin.site.register(Student,StudentAdmin)
