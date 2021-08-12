from django.contrib import admin
from django.urls import path
from .views import CountriesList

urlpatterns = [
    path('', CountriesList.as_view()),
    # path('', CountriesDetail.as_view()),
]