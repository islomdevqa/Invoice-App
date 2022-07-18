from django.http import HttpResponse
from django.shortcuts import render
from invoice_app.models import Invoice

def hello_world(request):
    obj = Invoice.objects.get(id=1)
    qs = Invoice.objects.all()
    context = {
        'obj_':obj,
        'qs':qs,
    }
    return render(request, 'home.html', context)