from rest_framework import serializers
from .models import*
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('title','image','id')
class DistrictSerializers(serializers.ModelSerializer):
    class Meta:
        model=Districts
        fields=('title','id')