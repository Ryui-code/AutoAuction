from django_filters import FilterSet
from .models import Car

class CarFilterSet(FilterSet):
    class Meta:
        model = Car
        fields = {
            'brand': ['exact'],
            'model': ['exact'],
            'year': ['gte', 'lte'],
            'transmission': ['exact'],
            'fuel_type': ['exact'],
            'price': ['gte', 'lte'],
            'mileage': ['lt', 'gt']
        }