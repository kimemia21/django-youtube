from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note,Users
from .serializer import NoteSerialzer,UserSerializer
from rest_framework import status
from django.contrib.auth import authenticate

@api_view(["GET"])
def getNotes(request):
    if request.method =='GET':
        obj =Note.objects.all()
        serializer =NoteSerialzer(obj,many=True)
        return Response(serializer.data)
    
@api_view(["GET"])
def getNote(request,pk):
    if request.method =='GET':
        note =Note.objects.get(id=pk)
        serializer =NoteSerialzer(note,many=False)
        return Response(serializer.data)    

@api_view(["POST"])
def AddNote(request):
    if request.method =='POST':
        data =request.data
        serializer =NoteSerialzer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        else:
            
            return Response(serializer.errors)  
@api_view(["PUT"])
def UpdateNote(request,pk):
    if request.method =='PUT':
        note =Note.objects.get(id=pk)
        serializer =NoteSerialzer(note, data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        else:
            
            return Response(serializer.errors)


@api_view(["DELETE"])
def NoteDelete(request,pk):
    if request.method =="DELETE":
        obj =Note.objects.get(id=pk)
        obj.delete()
        return Response("noted Delted")
    
    
@api_view(["POST"])
def loginUser(request):
    data = request.data
    username = data.get("userName")
    password = data.get("password")
    obj =Users.objects.get(userName =username)
    if obj.DoesNotExist:
        return Response("user not found", status=status.HTTP_400_BAD_REQUEST)
    else:
        serialzer =UserSerializer(data=data,many=False)
        return Response(serialzer.data,status=status.HTTP_200_OK)


 
    
    
    
        
           
        
               
    


# Create your views here.
