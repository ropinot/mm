from django.db import models

class ActivityStatusModel(models.Model):
        status = models.CharField(max_length=20)

        def __unicode__(self):
                return self.status


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


class InterventionTypeModel(models.Model):
        intervention_type = models.CharField(max_length = 200)

        def __unicode__(self):
                return self.intervention_type


class ComponentStatusModel(models.Model):
        component_status = models.CharField(max_length = 200)

        def __unicode__(self):
                return self.component_status


class ActivitySheetModel(models.Model):
        entry_date = models.DateField(null=True, blank=True) #data segnalazione
        entry_time = models.TimeField(null=True, blank=True) #ora segnalazione
        requested_by = models.CharField(max_length=20, null=True, blank=True)  # TODO: Eredita dall'ID dello user?
        status = models.ForeignKey(ActivityStatusModel, null=True, blank=True)
        component = models.CharField(max_length=20, null=True, blank=True)
        # description = models.CharField(max_length=200, null=True, blank=True)

        internal_responsible = models.CharField(max_length=200, null=True, blank=True)
        num_internal_operators = models.IntegerField(default=0, null=True, blank=True)
        internal_intervention_time_days = models.IntegerField(null=True, blank=True)
        internal_intervention_time_hours = models.IntegerField(null=True, blank=True)
        internal_intervention_time_minutes = models.IntegerField(null=True, blank=True)
        internal_intervention_duration = models.IntegerField(null=True, blank=True)

        external_company = models.ForeignKey(ExternalMaintenanceCompanyModel, null=True, blank=True)
        external_responsible = models.CharField(max_length=200, null=True, blank=True)
        num_external_operators = models.IntegerField(default=0, null=True, blank=True)
        external_intervention_time_days = models.IntegerField(null=True, blank=True)
        external_intervention_time_hours = models.IntegerField(null=True, blank=True)
        external_intervention_time_minutes = models.IntegerField(null=True, blank=True)
        external_intervention_duration = models.IntegerField(null=True, blank=True)

        intervention_start_date = models.DateField(null=True, blank=True) #data inizio manutenzione
        intervention_start_time = models.TimeField(null=True, blank=True) #ora inizio manutenzione
        intervention_completion_date = models.DateField(null=True, blank=True) #data fine manutenzione
        intervention_completion_time = models.TimeField(null=True, blank=True) #ora fine manutenzione
        machine_down_time_days = models.IntegerField(null=True, blank=True)
        machine_down_time_hours = models.IntegerField(null=True, blank=True)
        machine_down_time_minutes = models.IntegerField(null=True, blank=True)
        machine_down_time_duration = models.IntegerField(null=True, blank=True)
        intervention_type = models.ForeignKey(InterventionTypeModel, null=True, blank=True)
        component_status =  models.ForeignKey(ComponentStatusModel, null=True, blank=True)
        intervention_description = models.TextField(max_length=500, null=True, blank=True)


