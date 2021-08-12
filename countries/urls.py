from django.contrib import admin
from django.urls import path
from .views import CountriesList, CountriesDetail

urlpatterns = [
    # path('', CountriesList.as_view()),
    path('', CountriesDetail.as_view()),
]