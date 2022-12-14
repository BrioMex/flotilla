from django.contrib import admin

# Register your models here.
from .models import Vehicle, MyClubUser


@admin.register(Vehicle)#, EventAdmin)
class VehicleAdmin(admin.ModelAdmin):
    fields = ('owner', 'plate', ('lat', 'lon') )
    list_display = ('owner', 'plate', 'lat', 'lon')
    list_filter = ('owner', 'plate')
    ordering = ('plate',)


admin.site.register(MyClubUser)