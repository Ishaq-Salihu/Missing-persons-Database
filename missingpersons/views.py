from rest_framework import viewsets, permissions
from .models import Missingperson
from .serializers import MissingSerializer

class MissingApiView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Missingperson.objects.all()
    serializer_class = MissingSerializer
