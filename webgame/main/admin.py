from django.contrib import admin
from .models import *

@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Workers)

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass

@admin.register(Fabric)
class FabricAdmin(admin.ModelAdmin):
    pass

@admin.register(Users_resources)
class Users_resourcesAdmin(admin.ModelAdmin):
    list_display=('Resource', 'Sum')
