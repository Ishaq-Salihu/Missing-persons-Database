from rest_framework import viewsets, permissions
from .models import Missingperson
from .serializers import MissingSerializer
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator


class MissingApiView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Missingperson.objects.all()
    serializer_class = MissingSerializer
class MissingPersonListView(ListView):
    template_name = 'index.html'
    models = Missingperson
    paginate_by = 10
    queryset = Missingperson.objects.all()
