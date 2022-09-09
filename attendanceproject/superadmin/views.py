from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def AdminHome(request):
    return render(request, 'superadmin/index.html')