from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_name = 'perfume'

urlpatterns = [
    path('male/', views.PerfumeListView.as_view(), name='male'),
    path('female/', views.PerfumeListView.as_view(), name='female'),
    path('', RedirectView.as_view(url='/male/')),
    path('<int:pk>/', views.ParfumeDetailView.as_view(), name='detail')
]
