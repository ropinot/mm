from django.shortcuts import render
from mmsupplierDB.forms import ExternalMaintenanceCompanyForm
from mmsupplierDB.models import ExternalMaintenanceCompanyModel
from django.http import HttpResponse
# Create your views here.

def add_external_company(request):
        form = ExternalMaintenanceCompanyForm(request.POST or None)

        if form.is_valid():
                form.save()
                return render(request, 'mmmain/index.html')
        else:
                return render(request, 'mmsupplierDB/add_external_company.html', {'form': form})

def list_external_company(request):
        return HttpResponse("<h2>Funzionalita non ancora implementata</h2><br><a href='/mmmain'>Torna a Home</a>")
