from django import forms
from .models import Invoice
from django.core.exceptions import ValidationError

class InvoiceForm(forms.ModelForm):
    completion_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), label="Completion date")
    issue_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), label="Issue date")
    payment_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), label="Payment date")

    class Meta:
        model = Invoice
        fields = ('receiver', 'number', 'completion_date', 'issue_date', 'payment_date')
        labels = {
            "receiver": "Receiver",
            "number": "Number",
        }

    def clean_number(self):
        number = self.cleaned_data.get('number')
        if len(number) < 10:
            raise ValidationError("Number is too short !")
        return number
