from django.urls import path
from .views import getNotes,getNote,AddNote,UpdateNote

urlpatterns = [
    path('notes/',getNotes),
    path('notes/<str:pk>/',getNote),
    path('update/<str:pk>/',UpdateNote),
    path('addNotes',AddNote)
    
]

