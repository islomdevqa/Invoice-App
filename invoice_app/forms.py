from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('receiver', 'number', 'completion_date', 'issue_date', 'payment_date')
