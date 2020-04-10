from django.db import models


# Create your models here.

class DepartmentModel(models.Model):
    department_name = models.CharField(max_length=255, null=True, blank=True, unique=False)
    department_code = models.CharField(max_length=255, null=True, blank=True, unique=True)

    class Meta:
        db_table = 'tbl_department'
        verbose_name = 'Phòng ban'


class PersonModel(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True, unique=False)
    mid_name = models.CharField(max_length=255, null=True, blank=True, unique=False)
    last_name = models.CharField(max_length=255, null=True, blank=True, unique=False)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_ad = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(null=True, blank=True, default=False)
    is_active = models.BooleanField(null=True, blank=True, default=True)
    department = models.ForeignKey(DepartmentModel, null=True, blank=True,
                                   on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_employees'
        verbose_name = 'Nhan Vien'
