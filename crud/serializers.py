from rest_framework import serializers
from crud.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'p_name', 'p_description', 'price', 'created', 'updated']  