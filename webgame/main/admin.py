from django.contrib import admin
from .models import *

@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    list_display=('Resource','Price','Efficiency')


@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    list_display=('Created_resource','Level','User')

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display=('Name', 'Level','Experience')

@admin.register(Fabric)
class FabricAdmin(admin.ModelAdmin):
    list_display=('Name','Used_resource','Product')

@admin.register(Users_resources)
class Users_resourcesAdmin(admin.ModelAdmin):
    list_display=('Resource', 'Sum', 'User')


@admin.register(Users_fabric)
class Users_fabricAdmin(admin.ModelAdmin):
    list_display=('Fabric', 'Level', 'User','is_active')