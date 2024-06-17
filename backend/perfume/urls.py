from django.urls import path
from . import views

urlpatterns = [
    path('', views.PerfumeListView.as_view(), name='index'),
]
