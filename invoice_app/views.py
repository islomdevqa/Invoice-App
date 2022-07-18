from django.shortcuts import render
from django.views.generic import ListView
from .models import Invoice

# Create your views here.
class InvoiceListView(ListView):
    model = Invoice
    # template_name = "invoice_app/main.html" #default invoice_list.html
    # paginate_by
    # context_object_name = 'qs'