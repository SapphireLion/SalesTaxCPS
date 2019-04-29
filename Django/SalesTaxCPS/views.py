from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

import SalesTaxCPS.scripts.dataVisualization

# Create your views here.

def index(request):
    return HttpResponse("Hello Django!")
