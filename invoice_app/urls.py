from django.urls import path
from .views import InvoiceListView

app_name = 'invoice_app'

urlpatterns = [
    path('', InvoiceListView.as_view(), name='main')
]