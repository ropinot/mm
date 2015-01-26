from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from mmlog.forms import ActivitySheetForm
from mmlog.models import ActivitySheetModel


def index(request):
        return render(request, 'mmlog/index.html')


# def add_activity_sheet(request):
#         if request.method == 'POST':
#                 form = ActivitySheetForm(request.POST)
#                 if form.is_valid():
#                         form.save()
#                         return render(request, 'mmlog/index.html')
#                         # return index(request) #SOSTITUIRE CON REDIRECT???
#                 else:
#                         context = {'title': 'TITOLO DI PROVA', 'form': form}
#                         return render(request, 'mmlog/add_activity_sheet.html', context)
#
#         else:
#                 form = ActivitySheetForm()
#                 context = {'title': 'TITOLO DI PROVA', 'form': form}
#                 return render(request, 'mmlog/add_activity_sheet.html', context)

def add_activity_sheet(request):

        form = ActivitySheetForm(request.POST or None)
        if form.is_valid():
                form.save()
                return render(request, 'mmmain/index.html')
                # return index(request) #SOSTITUIRE CON REDIRECT???
        else:
                context = {'title': 'ERRORE NEL SALVATAGGIO', 'form': form}
                return render(request, 'mmlog/add_activity_sheet.html', context)


def update_activity(request, pk=None):
    obj = get_object_or_404(ActivitySheetModel, pk=13)
    form = ActivitySheetForm(request.POST or None, instance=obj)

    if request.method == 'POST':
        if form.is_valid():
           form.save()
           return redirect('mmmain/index.html')
    return render(request, 'mmlog/add_activity_sheet.html', {'form': form})



def list_activity_sheets_by_date(request):
        activity_sheets = ActivitySheetModel.objects.all().order_by('entry_date')
        context = {'activity_sheets': activity_sheets}
        return render(request, 'mmlog/list_activity_sheets_by_date.html', context)


def create_tree(request):

        return render(request, 'mmlog/create_tree.html')