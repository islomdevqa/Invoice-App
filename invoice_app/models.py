from django.db import models
from profile_app.models import Profile
from receiver_app.models import Receiver

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class Invoice(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    number = models.CharField(max_length=150)
    completion_date = models.DateField()
    issue_date = models.DateField()
    payment_date = models.DateField()
    created_time = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"Invoice number: {self.number}, pk: {self.pk}"

    def get_positions(self):
        pass

    def get_total_amount(self):
        pass
