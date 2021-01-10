from django.urls import path
from .views import MissingPersonListView

urlpatterns = [
    path('',MissingPersonListView.as_view(),name='home')
]