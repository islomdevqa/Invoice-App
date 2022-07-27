from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    FormView,
    TemplateView
)
from .models import Invoice
from profile_app.models import Profile
from .forms import InvoiceForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class InvoiceListView(LoginRequiredMixin, ListView):
    model = Invoice
    template_name = "invoice_app/main.html"
    # paginate_by
    context_object_name = 'qs'

    def get_queryset(self):
        # profile = Profile.objects.get(user=self.request.user)
        profile = get_object_or_404(Profile, user=self.request.user)
        qs = Invoice.objects.filter(profile=profile).order_by('-created_time')
        # return qs
        return super().get_queryset().filter(profile=profile).order_by('-created_time')

class InvoiceFormView(LoginRequiredMixin, FormView):
    form_class = InvoiceForm
    template_name = 'invoice_app/create.html'
    # success_url = reverse_lazy("invoice_app:main")
    i_instance = None

    def get_success_url(self):
        return reverse('invoice_app:simple-template', kwargs={'pk':self.i_instance.pk})

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        instance = form.save(commit=False)
        instance.profile = profile
        form.save()
        self.i_instance = instance
        return super().form_valid(form)

class SimpleTemplateView(TemplateView):
    template_name = 'invoice_app/simple_template.html'

