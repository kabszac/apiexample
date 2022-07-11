from rest_framework import serializers
from .models import Flavour

class FlavourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flavour
        fields = ['id', 'url','name', 'orders' ]

