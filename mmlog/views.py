from django.shortcuts import render, get_object_or_404, render_to_response
from django.db.models import F
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from mmlog.forms import ActivitySheetForm
from mmlog.models import ActivitySheetModel
from mmplantDB.models import PlantModel


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

def add_activity_sheet(request, sheet_type):
        """
        :param request:
        :param sheet_type: preventiva (100), correttiva (200), ispettiva (300)
        :return:
        """
        # tree = get_parent_of()

        tree = ""
        form = ActivitySheetForm(request.POST or None, initial={'sheet_type': sheet_type, 'requested_by': request.user.first_name +" "+request.user.last_name})
        form.fields['component'].widget.attrs['readonly'] = True
        if form.is_valid():
                form.save()
                return render(request, 'mmmain/index.html')
                # return index(request) #SOSTITUIRE CON REDIRECT???
        else:
                context = {'title': '', 'form': form, 'form_action': '/mmlog/add_activity_sheet/'+sheet_type, 'sheet_type': sheet_type, 'tree':tree} #TODO: il contenuto di tree deve essere l'albero dell'impianto
                return render(request, 'mmlog/add_activity_sheet.html', context)


def update_activity(request, id=None):

        obj = get_object_or_404(ActivitySheetModel, id=id)

        if request.method == 'POST':

                form = ActivitySheetForm(request.POST or None, instance=obj)
                if form.is_valid():
                        form.save()

                        # for v in a.__dict__:
                        #         print v, ": ", a.__dict__[v]
                        return render(request, 'mmmain/index.html')
                else:
                        # TODO: portare fuori il context dall'if in modo che vada bene per tutti i casi
                        context = {'title': '', 'form': form, 'form_action': '/mmlog/update_activity/'+id, 'sheet_type': obj.__dict__['sheet_type']}
                        return render(request, 'mmlog/add_activity_sheet.html', context)

        else:

                form = ActivitySheetForm(instance=obj)
                return render(request, 'mmlog/add_activity_sheet.html', {'form': form, 'form_action': '/mmlog/update_activity/'+id, 'sheet_type': obj.__dict__['sheet_type']})


def list_activity_sheets_by_date(request):
        activity_sheets = ActivitySheetModel.objects.all().order_by('entry_date')
        context = {'activity_sheets': activity_sheets}
        return render(request, 'mmlog/list_activity_sheets_by_date.html', context)


def create_tree(request):

        return render(request, 'mmlog/create_tree.html')

def get_parent_of(parentid=None):
        if parentid == None:
                obj = PlantModel.objects.filter(pk=F('parent'))
        else:
                obj = PlantModel.objects.filter(parent=parentid)

        tree = "<ul>"
        for o in obj:
                tree += "<li>"
                tree += o.component
                tree += "</li>"

        tree += "</ul>"
        print tree
        return tree