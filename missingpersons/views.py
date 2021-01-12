from rest_framework import viewsets, permissions
from .models import Missingperson, Comment
from .serializers import MissingSerializer
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q 

class MissingApiView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Missingperson.objects.all()
    serializer_class = MissingSerializer
class MissingPersonListView(ListView):
    template_name = 'index.html'
    model = Missingperson
    paginate_by = 10
    queryset = Missingperson.objects.all()
class MissingPersonCreateView(LoginRequiredMixin, CreateView):
    model = Missingperson
    template_name = 'PostNew.html'
    fields = ('__all__')
class MissingPersonDetailView(DetailView):
    model = Missingperson
    template_name = 'details.html'
class SearchResultsListView(ListView): 
    model = Missingperson
    template_name = 'search_results.html'
    def get_queryset(self): 
        query = self.request.GET.get('q')
        return Missingperson.objects.filter(
            Q(Name__icontains=query) )
class CreateComment(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = 'details.html'
    fields = ('comment')