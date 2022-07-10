from django.contrib import admin
from .models import Receiver
from import_export import resources
from import_export.admin import ExportActionMixin

# Register your models here.
class ReceiverResource(resources.ModelResource):
    class Meta:
        model = Receiver
        fields = "__all__"
        # export_order = ('website', 'created_time', 'address', 'name', 'id')

class ReceiverAdmin(ExportActionMixin, admin.ModelAdmin):
    resources_class = ReceiverResource

admin.site.register(Receiver, ReceiverAdmin)