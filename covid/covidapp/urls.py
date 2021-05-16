from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name="index"),
    path('see/<int:hospital_id>',views.see,name="see")
]