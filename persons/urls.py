from django.urls import path
from . import views

urlpatterns = [
    path('FamilyTree/persons/templates/persons/Mahdi.html' , views.mahdi),
    path('FamilyTree/persons/templates/persons/FahimeSadat.html' , views.fahimesadat),
    path('FamilyTree/persons/templates/persons/Abolfazl.html' , views.abolfazl),
    path('FamilyTree/persons/templates/persons/Amir.html' , views.amir),
    path('FamilyTree/persons/templates/persons/Zohreh.html' , views.zohre),
    path('FamilyTree/persons/templates/persons/Mamani.html' , views.mamani),
    path('FamilyTree/persons/templates/persons/Fatima.html' , views.fatima),
    path('FamilyTree/persons/templates/persons/Babaee.html' , views.babaee),
    path('FamilyTree/persons/templates/persons/Javad.html' , views.javad),
    path('FamilyTree/persons/templates/persons/Fahime.html' , views.fahime),
    path('FamilyTree/persons/templates/persons/Maryam.html' , views.maryam),
    path('FamilyTree/persons/templates/persons/Mohsen.html' , views.mohsen),
    path('FamilyTree/persons/templates/persons/Taha.html' , views.taha),
    path('FamilyTree/persons/templates/persons/Sana.html' , views.sana),
    path('FamilyTree/persons/templates/persons/Tasnim.html' , views.tasnim),
]