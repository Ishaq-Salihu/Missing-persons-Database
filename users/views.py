from rest_framework import viewsets, permissions

from .models import CustomUser
from .serializers import Userserializer

class UserViewSet(viewsets.ModelViewSet):
    #permission_classes = (permissions.IsAdminUser,)
    queryset = CustomUser.objects.all()
    serializer_class = Userserializer

