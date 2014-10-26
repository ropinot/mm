from django.db import models

class ActivityStatusModel(models.Model):
        status = models.CharField(max_length=20)

        def __unicode__(self):
                return self.status


class ExternalMaintenanceCompanyModel(models.Model):
        company = models.CharField(max_length=200)
        responsible = models.CharField(max_length=200)
        num_operators = models.IntegerField()
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
        entry_date = models.DateField(null=True) #data segnalazione
        entry_time = models.TimeField(null=True) #ora segnalazione
        component = models.CharField(max_length=20)
        description = models.CharField(max_length=200)
        status = models.ForeignKey(ActivityStatusModel, null=True)
        internal_responsible = models.CharField(max_length=200)
        num_internal_operators = models.IntegerField(default=0)
        internal_intervention_time_days = models.IntegerField(null=True)
        internal_intervention_time_hours = models.IntegerField(null=True)
        internal_intervention_time_minutes = models.IntegerField(null=True)
        internal_intervention_duration = models.IntegerField(null=True)

        external_company = models.ForeignKey(ExternalMaintenanceCompanyModel, null=True)
        external_responsible = models.CharField(max_length=200)
        num_external_operators = models.IntegerField(default=0)
        external_intervention_time_days = models.IntegerField(null=True)
        external_intervention_time_hours = models.IntegerField(null=True)
        external_intervention_time_minutes = models.IntegerField(null=True)
        external_intervention_duration = models.IntegerField(null=True)

        intervention_start_date = models.DateField(null=True) #data inizio manutenzione
        intervention_start_time = models.TimeField(null=True) #ora inizio manutenzione
        intervention_completion_date = models.DateField(null=True) #data fine manutenzione
        intervention_completion_time = models.TimeField(null=True) #ora fine manutenzione
        machine_down_time_days = models.IntegerField(null=True)
        machine_down_time_hours = models.IntegerField(null=True)
        machine_down_time_minutes = models.IntegerField(null=True)
        machine_down_time = models.IntegerField(null=True)
        intervention_type = models.ForeignKey(InterventionTypeModel, null=True)
        component_status =  models.ForeignKey(ComponentStatusModel, null=True)
        intervention_description = models.CharField(max_length=500)


