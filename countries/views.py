from django.shortcuts import render
from .models import Countries
from .serializers import  CountriesSerializer
from rest_framework import generics
# Create your views here.

class CountriesList(generics.ListCreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


# class CountriesDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Countries.objects.all()
#     serializer_class = CountriesSerializer
