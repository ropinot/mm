from django import forms
from django.forms import widgets as w
from mmlog.models import *
from mmsupplierDB.models import *

import time
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


# class ActivityForm(forms.Form):
#         name = forms.CharField(label = "Nome", max_length = 100)
#         surname = forms.CharField(label = "Cognome", max_length = 100)

class ActivitySheetForm(forms.ModelForm):
        # MODIFICA DEL WIDGET STANDARD PER I CAMPI DEL DB

        sheet_type = forms.CharField(widget=w.HiddenInput, required=False)

        entry_date = forms.DateField(label="Data segnalazione", initial=time.strftime("%d/%m/%Y"))
        entry_time = forms.TimeField(label="Ora segnalazione", initial=time.strftime("%H:%M"))
        component = forms.CharField(max_length=100, label="Componente")
        requested_by = forms.CharField(max_length=20, label="Richiedente")
        # description = forms.CharField(max_length=100, label="Descrizione dell'intervento")
        status = forms.ModelChoiceField(ActivityStatusModel.objects.all(), label="Stato", initial=0)
        internal_responsible = forms.CharField(max_length=20, label="Responsabile")
        num_internal_operators = forms.CharField(widget=w.NumberInput, label="N. Oper.", initial=0)
        internal_intervention_time_days = forms.CharField(max_length=4, label="Giorni", initial=0, required=False)
        internal_intervention_time_hours = forms.CharField(max_length=4, label="Ore", initial=0, required=False)
        internal_intervention_time_minutes = forms.CharField(max_length=4, label="Minuti", initial=0, required=False)
        internal_intervention_duration = forms.CharField(max_length=4, label="Totale (minuti)", initial=0, required=False)

        external_company = forms.ModelChoiceField(ExternalMaintenanceCompanyModel.objects.all(), label="Azienda", required=False)
        external_responsible = forms.CharField(max_length=200, label="Responsabile", required=False)
        num_external_operators = forms.CharField(widget=w.NumberInput, label="N. Oper.", required=False, initial=0)
        external_intervention_time_days = forms.CharField(max_length = 4, label="Giorni", required=False, initial=0)
        external_intervention_time_hours = forms.CharField(max_length = 4, label="Ore", required=False, initial=0)
        external_intervention_time_minutes = forms.CharField(max_length = 4, label="Minuti", required=False, initial=0)
        external_intervention_duration = forms.CharField(max_length = 4, label="Totale (minuti)", required=False, initial=0)

        intervention_start_date = forms.DateField(label="Data inizio", required=False) #data inizio manutenzione
        intervention_start_time = forms.TimeField(label="Ora inizio", required=False) #ora inizio manutenzione
        intervention_completion_date = forms.DateField(label="Data fine", required=False) #data fine manutenzione
        intervention_completion_time = forms.TimeField(label="Ora fine", required=False) #ora fine manutenzione
        machine_down_time_days = forms.CharField(label="Giorni", required=False, initial=0)
        machine_down_time_hours = forms.CharField(label="Ore", required=False, initial=0)
        machine_down_time_minutes = forms.CharField(label="Minuti", required=False, initial=0)
        machine_down_time_duration = forms.CharField(label="Totale (minuti)", required=False, initial=0)

        intervention_description = forms.CharField(widget=forms.Textarea, label="Descrizione dell'intervento", required=False)

        # Intervento preventiva
        intervention_type = forms.ModelChoiceField(InterventionTypeModel.objects.all(), label="Tipo intervento", required=False)
        component_status =  forms.ModelChoiceField(ComponentStatusModel.objects.all(), label="Stato componente", required=False)


        # Intervento correttiva
        fault_type = forms.ModelChoiceField(FaultTypeModel.objects.all(), label="Tipo di guasto", required=False)
        fault_cause = forms.ModelChoiceField(FaultCauseModel.objects.all(), label="Causa di guasto", required=False)
        fault_effect = forms.ModelChoiceField(FaultEffectModel.objects.all(), label="Effetto del guasto", required=False)
        fault_description = forms.CharField(widget=forms.Textarea, label="Descrizione del guasto", required=False)


        # Intervento ispettiva
        measurements = forms.CharField(widget=forms.Textarea, label="Valori misurati", required=False)


        class Meta:
                # MODELLO ASSOCIATO
                model = ActivitySheetModel
                fields = '__all__'

                # LISTA CAMPI VISIBILI NEL FORM
                # fields =  ['entry_date', 'intervention_type']


# class ActivitySheetForm(forms.ModelForm):
#
#         # MODIFICA DEL WIDGET STANDARD PER I CAMPI DEL DB
#         entry_date = forms.CharField(max_length=10, label="Data")
#         entry_time = forms.TimeField(label='Ora') #ora segnalazione
#         component = forms.CharField(max_length=20, label='Componente')
#         description = forms.CharField(max_length=200)
#         # internal_responsible = forms.CharField(max_length=200)
#         # num_internal_operators = forms.IntegerField()
#         # internal_intervention_time_days = forms.IntegerField()
#         # internal_intervention_time_hours = forms.IntegerField()
#         # internal_intervention_time_minutes = forms.IntegerField()
#         # internal_intervention_duration = forms.IntegerField()
#
#         class Meta:
#                 # MODELLO ASSOCIATO
#                 model = ActivitySheetModel
#
#                 # LISTA CAMPI VISIBILI NEL FORM
#                 fields =  ['entry_date', 'entry_time', 'component', 'description']
#
#         def __init__(self, *args, **kwargs):
#                 super(ActivitySheetForm, self).__init__(*args, **kwargs)
#                 self.helper = FormHelper()
#                 self.helper.layout = Layout(
#                         Fieldset('Intervento',
#                                  'entry_date',
#                                  'entry_time'),
#                         Fieldset('Responsabile',
#                                  'component',
#                                  'description'),
#                         ButtonHolder(
#                                 Submit('submit', 'Submit', css_class='button white')
#                                 ))
#                 # self.helper.form_id = 'id_add_activity_sheet_form'
#                 # self.helper.form_method = 'POST'
#                 # self.helper.form_action = '/mmlog/add_activity_sheet/'
#                 # self.helper.add_input(Submit('submit', 'Submit'))
