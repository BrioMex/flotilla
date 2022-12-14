from django.forms import ModelForm
from .models import Vehicle

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ('plate', 'lon', 'lat')
        labels = {
            'plate' : 'plate',
            'lon' : 'lon',
            'lat' : 'lat',
        }