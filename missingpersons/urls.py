from django.urls import path
from .views import MissingPersonListView, MissingPersonCreateView, MissingPersonDetailView, SearchResultsListView, CreateComment

urlpatterns = [
    path('',MissingPersonListView.as_view(), name='home'),
    path('PostNew/', MissingPersonCreateView.as_view(), name='postnew'),
    path('<uuid:pk>', MissingPersonDetailView.as_view(), name='missingdetails'),
    path('<uuid:pk>/comments/', CreateComment.as_view(), name='Comments'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]