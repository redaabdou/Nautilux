
from django.db.models import fields
from rest_framework import serializers
from .models import Category, Equipment
  
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'description', 'parent')
  
class EquipmentSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Equipment
        fields = ('name', 'slug', 'categories', 'quantity')

class EquipmentSerializerForPagination(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('name', 'slug', 'categories', 'quantity')