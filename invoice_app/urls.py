from django.urls import path
from .views import (
    InvoiceListView,
    InvoiceFormView,
)

app_name = 'invoice_app'

urlpatterns = [
    path('', InvoiceListView.as_view(), name='main'),
    path('new/', InvoiceFormView.as_view(), name='create'),
]