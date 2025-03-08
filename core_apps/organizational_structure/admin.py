from django.contrib import admin

from core_apps.organizational_structure.models import Floor

# Register your models here.
class FloorAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'status', 'description')
    search_fields = ( 'id',  'status', 'description')
    list_filter = ( 'id',  'status', 'description')


admin.site.register(Floor, FloorAdmin)
