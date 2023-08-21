from django.db import models


# Create your models here.
class Dashboard(models.Model):
    work_order = models.CharField(max_length=20, blank=True, null=True)
    gap = models.CharField(max_length=100, blank=True, null=True)
    data_time = models.DateTimeField()
    operator_remarks = models.CharField(max_length=100, blank=True, null=True)



    class Meta:
        verbose_name = "Dashboard"
        verbose_name_plural = "Dashboards"