from django.shortcuts import render, HttpResponse
from mmplantDB.models import PlantModel
# Create your views here.


def index(request):
        return HttpResponse("<h1>TUtto Ok</h1>")


def get_children(request, parent_id=0):
        if parent_id == -1:
                # return HttpResponse("<h1>Get -1</h1>")
                obj = PlantModel.objects.filter(pk=F('parent'))
        else:
                # return HttpResponse("<h1>Get {} </h1>".format(parent_id))
                obj = PlantModel.objects.filter(parent=parent_id)

        tree = "<ul>"
        for o in obj:
                tree += "<li>"
                tree += o.component
                tree += "</li>"

        tree += "</ul>"
        # print tree
        return HttpResponse(tree)