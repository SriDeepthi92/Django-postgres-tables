from django.shortcuts import render
from .models import *
from django.http import HttpResponse
 
 
def index(request):
   return render(request, 'index.html')

def table(request):
    columns = GpdbCpTable.objects.all()
    return render(request, 'table.html', {'columns': columns})