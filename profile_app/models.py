from django.db import models
from django.contrib.auth.models import User
from .utils import generate_account_number

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=12, blank=True)
    company_name = models.CharField(max_length=200)
    company_info = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of: {self.user.username}"

    def save(self, *args, **kwargs):
        if self.account_number == "":
            self.account_number = generate_account_number()
        return super().save(*args, **kwargs)

    # def clean(self):
    #     if len(self.account_number) != 12:
    #         raise ValidationError("Bank account number must be 12 character long!")
