from django.db import models

class State(models.Model):
    name = models.CharField(max_length=15,null=False,blank=False)

    def __str__(self):
        return self.name
    
class City(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    name = models.CharField(max_length=15,null=False,blank=False)    

    class Meta:
        verbose_name = 'City'
        verbose_name_plural ='Cities'

    def __str__(self):
        return self.name
    
class Hospital(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    phone = models.IntegerField(null=False,blank=False)
    address = models.TextField(max_length=500,null=False,blank=False)
    state = models.ForeignKey(State,null=False,blank=False,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE,null=False,blank=False)

    @staticmethod
    def get_hospitals(cityid):
        if cityid:  
            return Hospital.objects.filter(city=cityid)
        else:
            return Hospital.objects.all()

    def __str__(self):
        return self.name
        
class Facility(models.Model):
    # hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,null=False,blank=False,default="")

    class Meta:
        verbose_name_plural='facilities'

    def __str__(self):
        return self.title

class Availability(models.Model):
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE,related_name="availabilities")
    facility = models.ForeignKey(Facility,on_delete=models.CASCADE,related_name="facilities")
    total = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Availibilities'
    
    def __str__(self):
        return self.hospital.name