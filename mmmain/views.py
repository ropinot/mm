from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
# @method_decorator(login_required)
@login_required
def index(request):
        return render(request, 'mmmain/index.html')
