from django.contrib import admin
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

# Register your models here.

@receiver(post_save,sender=Hospital)
def afterhospitalsave(signal,instance,**kwargs):
    facilities = Facility.objects.all()
    for facility in facilities:
        availability = Availability(hospital=instance,facility=facility)
        availability.save()

class HospitalAdmin(admin.ModelAdmin):
    model = Hospital
    list_display=['name','state','city','phone','address']

class FacilityAdmin(admin.ModelAdmin):
    model = Facility
    list_display=['hospital','totaloxygenbeds','availableoxygenbeds','totaloxygencylinder','availableoxygencylinder','totalventilator','availableventilator']

class AvailabilityAdmin(admin.ModelAdmin):
    model = Availability
    list_display = ['hospital','facility','total','available','updated_at']
    list_editable=['total','available']

admin.site.register(State)
admin.site.register(City)
admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Facility)
admin.site.register(Availability,AvailabilityAdmin)