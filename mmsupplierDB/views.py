from django.shortcuts import render, get_object_or_404
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

def list_external_companies(request):
        # return HttpResponse("<h2>Funzionalita non ancora implementata</h2><br><a href='/mmmain'>Torna a Home</a>")
        companies = ExternalMaintenanceCompanyModel.objects.all()
        context = {'companies': companies}
        return render(request, 'mmsupplierDB/list_companies.html', context)

def update_company(request, id):
        obj = get_object_or_404(ExternalMaintenanceCompanyModel, id=id)

        if request.method == 'POST':
                form = ExternalMaintenanceCompanyForm(request.POST or None, instance=obj)
                if form.is_valid():
                        form.save()
                        return render(request, 'mmmain/index.html')
                else:
                        context = {'title': 'ERRORE NEL SALVATAGGIO', 'form': form, 'form_action': '/mmsupplierDB/update_company/'+id}
                        return render(request, 'mmsupplierDB/add_external_company.html', context)

        else:
                form = ExternalMaintenanceCompanyForm(instance=obj)
                return render(request, 'mmsupplierDB/add_external_company.html', {'form': form, 'form_action': '/mmsupplierDB/update_company/'+id})
