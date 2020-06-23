from django.contrib import admin
from testapp.models import ContactInfo3,StudentIII,TeacherIII,Parent1,Child,SubChild

# Register your models here.
# class ContactInfo3Admin(admin.ModelAdmin):
#     list_display=['name','email','address']
#
# class StudentIIIAdmin(admin.ModelAdmin):
#     list_display=['name','email','address','rollno','marks']
#
# class TeacherIIIAdmin(admin.ModelAdmin):
#     list_display=['name','email','address','subjects','salary']

admin.site.register(ContactInfo3)
admin.site.register(StudentIII)
admin.site.register(TeacherIII)
admin.site.register(Parent1)
admin.site.register(Child)
admin.site.register(SubChild)
