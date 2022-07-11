from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Flavour
from .serializers import FlavourSerializer

# Create your views here.
class Flavourview(viewsets.ModelViewSet):
    #how to get the objects from db
    # serializer
    queryset = Flavour.objects.all()
    serializer_class = FlavourSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)