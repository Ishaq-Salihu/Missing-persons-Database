from rest_framework import serializers
from .models import Missingperson

class MissingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Missingperson
        fields = ('Name','Sex','age','state','lastseenat','description','image','id','uploaddate')