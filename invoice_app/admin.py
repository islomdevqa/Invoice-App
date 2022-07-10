from django.contrib import admin
from .models import Invoice, Tag
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin

# Register your models here.
class TagResource(resources.ModelResource):
    class Meta:
        model = Tag
        fields = ('id', 'name')

class TagAdmin(ExportActionMixin, admin.ModelAdmin):
    resources_class = TagResource

class InvoiceResource(resources.ModelResource):
    profile = Field()
    receiver = Field()

    class Meta:
        model = Invoice
        fields = "__all__"

    def dev_profile(self, obj):
        return obj.profile.user.username

    def dev_receiver(self, obj):
        return obj.receiver.name

class InvoiceAdmin(ExportActionMixin, admin.ModelAdmin):
    resources_class = InvoiceResource

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Tag, TagAdmin)
