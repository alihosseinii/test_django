from rest_framework.serializers import ModelSerializer
from .models import Train, City


class TrainSerializer(ModelSerializer):
    """serializer for trains"""
    class Meta:
        model = Train
        fields = [ 'id', 'traintype', 'depratortime', 'price', 'returntime', 'origin', 'destination', 'available']

class TrainDetailSerializer(ModelSerializer):
    """a serializer for train details """
    class Meta:
        model = Train 
        fields = "__all__"

class CitySerializer(ModelSerializer):
    """serializer for show the citeis name"""
    class Meta:
        model = City
        fields = "__all__"