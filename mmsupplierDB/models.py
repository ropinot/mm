from django.db import models

class ExternalCompanyStatus(models.Model):
        status = models.CharField(max_length=20)

        def __unicode__(self):
                return self.status


class ExternalMaintenanceCompanyModel(models.Model):
        company_name = models.CharField(max_length=200, null=True, blank=True)
        fiscal_code = models.CharField(max_length=15, null=True, blank=True)
        address = models.CharField(max_length=50, null=True, blank=True)
        status = models.ForeignKey(ExternalCompanyStatus, null=True, blank=True)
        registration_date = models.DateField() # timestamp

        def __unicode__(self):
                return self.company_name


