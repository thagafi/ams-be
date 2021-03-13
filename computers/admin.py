from django.contrib import admin
from .models import ComputersModel, CPUModel, RamSize, MonitorSize, OS, Brand

# Register your models here.

@admin.register(ComputersModel)
class ComputersAdmin(admin.ModelAdmin):
    readonly_fields = ['user']

    def get_form(self, request, obj=None, **kwargs):
        ComputersModel.user = request.user
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.user_id = request.user.id
        obj.last_modified_by = request.user
        obj.save()


@admin.register(CPUModel)
class CPUAdmin(admin.ModelAdmin):
    pass
@admin.register(RamSize)
class RamAdmin(admin.ModelAdmin):
    pass
@admin.register(MonitorSize)
class MonitorAdmin(admin.ModelAdmin):
    pass
@admin.register(OS)
class OSAdmin(admin.ModelAdmin):
    pass
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


