from django.shortcuts import render, HttpResponse
from django.db.models import F
from mmplantDB.models import PlantModel
# Create your views here.


def index(request):
        return HttpResponse("<h1>TUtto Ok</h1>")


def get_children(request, parent=0):
        if parent == 0:
                # return HttpResponse("<h1>Get -1</h1>")
                obj = PlantModel.objects.filter(id__exact=F('parent_id'))
        else:
                # return HttpResponse("<h1>Get {} </h1>".format(parent_id))
                obj = PlantModel.objects.filter(parent_id=parent)

        tree = "<ul>"
        for o in obj:
                tree += "<li>"
                tree += o.component
                tree += "</li>"

        tree += "</ul>"
        print tree
        return HttpResponse(tree)