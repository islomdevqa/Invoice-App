from django.http import HttpResponse
from django.shortcuts import render
from invoice_app.models import Invoice

def hello_world(request):
    obj = Invoice.objects.get(id=1)
    qs = Invoice.objects.all()
    return render(request, 'home.html')