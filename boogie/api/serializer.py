from rest_framework.serializers import ModelSerializer
from .models import Note,Users

class NoteSerialzer(ModelSerializer):
    class Meta:
        model =Note
        fields ="__all__"
        
class UserSerializer(ModelSerializer):
    class Meta:
        model=Users
        fields ="__all__"        
        
        
