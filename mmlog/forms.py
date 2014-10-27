from django import forms
from mmlog.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


# class ActivityForm(forms.Form):
#         name = forms.CharField(label = "Nome", max_length = 100)
#         surname = forms.CharField(label = "Cognome", max_length = 100)

class ActivitySheetForm(forms.Form):
        # MODIFICA DEL WIDGET STANDARD PER I CAMPI DEL DB
        entry_date = forms.CharField(max_length=10, help_text="Data in formato gg-mm-aaaa", label="Data")
        component = forms.CharField(max_length=100, label="Componente")
        description = forms.CharField(max_length=100, label="Descrizione")

        internal_intervention_time_days = forms.CharField(max_length=4, label="Giorni")
        internal_intervention_time_hours = forms.CharField(max_length=4, label="Ore")
        internal_intervention_time_minutes = forms.CharField(max_length=4, label="Minuti")
        internal_intervention_duration = forms.CharField(max_length=4, label="Totale")

        class Meta:
                # MODELLO ASSOCIATO
                model = ActivitySheetModel

                # LISTA CAMPI VISIBILI NEL FORM
                fields =  ['entry_date', 'intervention_type']


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
