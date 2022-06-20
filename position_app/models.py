from django.db import models
from invoice_app.models import Invoice

# Create your models here.
class Position(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, help_text="Optional info")
    amount = models.FloatField(help_text='in US $')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice: {self.invoice.number}, position title: {self.title}"
