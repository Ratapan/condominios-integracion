from django.urls import path
from .views import CondominiumView,ResidentView,HouseView,ResidenceView

urlpatterns = [
    path('condominiums/', CondominiumView.as_view(), name='condominium_list'),
    path('residents/', ResidentView.as_view(), name='resident_list'),
    path('houses/', HouseView.as_view(), name='house_list'),
    path('residences/', ResidenceView.as_view(), name='residence_list'),
]