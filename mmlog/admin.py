from django.contrib import admin
from mmlog.models import ActivityStatusModel, ExternalMaintenanceCompanyModel, InterventionTypeModel, ComponentStatusModel, ActivitySheetModel

admin.site.register(ActivityStatusModel)
admin.site.register(ExternalMaintenanceCompanyModel)
admin.site.register(InterventionTypeModel)
admin.site.register(ComponentStatusModel)
admin.site.register(ActivitySheetModel)

