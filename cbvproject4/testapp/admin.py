from django.contrib import admin
from testapp.models import StudentInfo

# Register your models here.
class StudentInfoAdmin(admin.ModelAdmin):
    list_display=['name','rollno','addr']

admin.site.register(StudentInfo,StudentInfoAdmin)
