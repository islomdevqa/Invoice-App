from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    FormView,
    TemplateView,
    DetailView,
    UpdateView
)
from .models import Invoice
from profile_app.models import Profile
from profile_app.forms import PositionForm
from .forms import InvoiceForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.
class InvoiceListView(LoginRequiredMixin, ListView):
    model = Invoice
    template_name = "invoice_app/main.html"
    paginate_by = 3
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
        return reverse('invoice_app:detail', kwargs={'pk':self.i_instance.pk})

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        instance = form.save(commit=False)
        instance.profile = profile
        form.save()
        self.i_instance = instance
        return super().form_valid(form)

class SimpleTemplateView(DetailView):
    model = Invoice
    template_name = 'invoice_app/simple_template.html'

class AddPositionsFormView(FormView):
    form_class = PositionForm
    template_name = 'invoices/detail.html'

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        invoice_pk = self.kwargs.get('pk')
        obj = Invoice.objects.get(pk=invoice_pk)
        instance = form.save(commit=False)
        instance.invoice = invoice_obj
        form.save()
        messages.info(self.request, f'Successfully added position - {instance.title}')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invoice_obj = Invoice.objects.get(pk=self.kwargs.get('pk'))
        qs = invoice_obj.positions
        context['obj'] = invoice_obj
        context['qs'] = qs
        return context
class InvoiceUpdateView(UpdateView):
    model = Invoice
    template_name = 'invoice_app/update.html'
    form_class = InvoiceForm
    success_url = reverse_lazy('invoice_app:main')

    def form_valid(self, form):
        instance = form.save()
        messages.info(self.request, f"Successfully updated invoice - {instance.number}")
        return super().form_valid(form)

