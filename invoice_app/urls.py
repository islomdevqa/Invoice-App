from django.urls import path
from .views import (
    InvoiceListView,
    InvoiceFormView,
    SimpleTemplateView,
    InvoiceUpdateView,
)

app_name = 'invoice_app'

urlpatterns = [
    path('', InvoiceListView.as_view(), name='main'),
    path('new/', InvoiceFormView.as_view(), name='create'),
    path('<pk>/', SimpleTemplateView.as_view(), name="simple-template"),
    path('<pk>/update/', InvoiceUpdateView.as_view(), name="update"),
]