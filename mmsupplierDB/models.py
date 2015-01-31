from django.db import models


# Create your models here.
class ExternalMaintenanceCompanyModel(models.Model):
        company = models.CharField(max_length=200, null=True, blank=True)
        # responsible = models.CharField(max_length=200, null=True, blank=True)
        # num_operators = models.IntegerField(null=True, blank=True)
        # intervention_time_days = models.IntegerField()
        # intervention_time_hours = models.IntegerField()
        # intervention_time_minutes = models.IntegerField()
        # intervention_duration = models.IntegerField()

        def __unicode__(self):
                return self.company