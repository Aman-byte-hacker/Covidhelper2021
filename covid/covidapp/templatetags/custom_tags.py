from covidapp.models import Availability
from django import template

register = template.Library()

@register.simple_tag
def get_class(value):
    if value:
        return 'bg-success'
    else:
        return 'bg-danger'    

@register.simple_tag
def get_availablities(hospital):
    return Availability.objects.filter(hospital=hospital).order_by('facility_id')
            