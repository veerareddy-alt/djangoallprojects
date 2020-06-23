from django.contrib import admin
from testapp.models import Employee,ProxyEmployee,ProxyEmployee2

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('eno','ename','esal','eaddr')

class ProxyEmployeeAdmin(admin.ModelAdmin):
    list_display=('eno','ename','esal','eaddr')

class ProxyEmployeeAdmin2(admin.ModelAdmin):
    list_display=('eno','ename','esal','eaddr')


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(ProxyEmployee,ProxyEmployeeAdmin)
admin.site.register(ProxyEmployee2,ProxyEmployeeAdmin2)
