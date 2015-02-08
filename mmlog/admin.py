from django.contrib import admin
from mmlog.models import ActivityStatusModel, InterventionTypeModel, ComponentStatusModel, ActivitySheetModel
from mmsupplierDB.models import ExternalMaintenanceCompanyModel
from mmplantDB.models import PlantModel

admin.site.register(ActivityStatusModel)
admin.site.register(ExternalMaintenanceCompanyModel)
admin.site.register(InterventionTypeModel)
admin.site.register(ComponentStatusModel)
admin.site.register(ActivitySheetModel)
admin.site.register(PlantModel)

