from rest_framework import serializers
from testapp.models import Products

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'  # All field into JSON / DRF formet