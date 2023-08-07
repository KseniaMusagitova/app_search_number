from django.db import models


# Create your models here.
class Dashboard(models.Model):
    serial_number = models.CharField(max_length=20, blank=True, null=True)
    operator_remarks = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.serial_number

    class Meta:
        verbose_name = "Dashboard"
        verbose_name_plural = "Dashboards"