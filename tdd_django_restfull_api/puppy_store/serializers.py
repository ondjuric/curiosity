"""
Represents models' serializers
"""
from rest_framework import serializers
from puppy_store.models import Puppy


class PuppySerializer(serializers.ModelSerializer):
    """
    Puppy Model Serializer.
    Validates the model queryset and produces Pythonic data types to work with.
    """
    class Meta:
        model = Puppy
        fields = ('name', 'age', 'breed', 'color', 'created_at', 'updated_at')
