from django.urls import path
from .views import getNotes,getNote,AddNote

urlpatterns = [
    path('notes/',getNotes),
    path('notes/<str:pk>/',getNote),
    path('addNotes',AddNote)
    
]

