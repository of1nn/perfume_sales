from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TemplateView.as_view(), name='index'),
]
