from django.contrib import admin
from .models import Profile
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin

# Register your models here.
class ProfileResource(resources.ModelResource):
    user = Field()
    class Meta:
        model = Profile
        fields = "__all__"

    def dehydrate_user(self, obj):
        return obj.user.username

class ProfileAdmin(ExportActionMixin, admin.ModelAdmin):
    resources_class = ProfileResource

admin.site.register(Profile, ProfileAdmin)