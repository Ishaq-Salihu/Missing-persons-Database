from django.urls import path
from .views import MissingPersonListView, MissingPersonCreateView, MissingPersonDetailView, SearchResultsListView 

urlpatterns = [
    path('',MissingPersonListView.as_view(), name='home'),
    path('PostNew/', MissingPersonCreateView.as_view(), name='postnew'),
    path('<uuid:pk>', MissingPersonDetailView.as_view(), name='missingdetails'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]