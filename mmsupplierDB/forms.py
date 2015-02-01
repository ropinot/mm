from django import forms
from django.forms import widgets as w
from mmlog.models import *
from mmsupplierDB.models import *

import time


class ExternalMaintenanceCompanyForm(forms.ModelForm):
        company_name = forms.CharField(label="Ragione sociale")
        fiscal_code = forms.CharField(label="P.Iva o CF")
        address = forms.CharField(label="Indirizzo")
        status = forms.ModelChoiceField(ExternalCompanyStatusModel.objects.all(), label="Stato", initial=0)
        registration_date = forms.DateField(label="Data inserimento", initial=time.strftime("%d/%m/%Y")) # timestamp

        class Meta:
                # MODELLO ASSOCIATO
                model = ExternalMaintenanceCompanyModel
                fields = '__all__'

