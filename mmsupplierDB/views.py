from django.shortcuts import render
from mmsupplierDB.forms import ExternalMaintenanceCompanyForm
from mmsupplierDB.models import ExternalMaintenanceCompanyModel

# Create your views here.

def add_external_company(request):
        form = ExternalMaintenanceCompanyForm(request.POST or None)

        if form.is_valid():
                form.save()
                return render(request, 'mmmain/index.html')
        else:
                return render(request, 'mmsupplierDB/add_external_company.html', {'form': form})

