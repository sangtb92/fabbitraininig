from django.contrib import admin

from employees.models import PersonModel, DepartmentModel


# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'mid_name', 'last_name',
                    'is_active', 'is_deleted', 'created_at', 'department']
    list_filter = ['department', 'is_active']
    search_fields = ['first_name']
    readonly_fields = ['department', 'is_active']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name', 'department_code']
    list_filter = ['department_code', ]
    search_fields = ['department_name', 'department_code']


admin.site.register(PersonModel, PersonAdmin)
admin.site.register(DepartmentModel, DepartmentAdmin)
