from django.urls import path
from .views import getNotes,getNote,AddNote,UpdateNote,NoteDelete,loginUser

urlpatterns = [
     path('login',loginUser),
    path('notes/',getNotes),
    path('notes/<str:pk>/',getNote),
    path('notes/<str:pk>/update',UpdateNote),
    path('notes/<str:pk>/delete',NoteDelete),
    
    path('notes/create',AddNote)
    
]

