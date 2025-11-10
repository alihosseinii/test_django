from rest_framework import serializers
from .models import Reservation, Passenger
from train.models import Train
from django.utils import timezone
from django.db import models

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['full_name', 'national_id']


class ReservationSerializer(serializers.ModelSerializer):
    passengers = PassengerSerializer(many=True)
    train = serializers.PrimaryKeyRelatedField(queryset=Train.objects.all())

    class Meta:
        model = Reservation
        fields = ['id', 'train', 'quantity', 'total_price', 'reserved_at', 'passengers']
        read_only_fields = ['total_price', 'reserved_at']

    def validate(self, data):
        train = data.get('train')
        quantity = data.get('quantity', 1)

        if train.depratortime <= timezone.now():
            raise serializers.ValidationError("The train has already departed.")
        
        reserved_count = Reservation.objects.filter(train=train).aggregate(total=models.Sum('quantity'))['total'] or 0
        available_seats = train.capacity - reserved_count
        if quantity > available_seats:
            raise serializers.ValidationError(f"Only {available_seats} seats remaining.")

        return data

    def create(self, validated_data):
        passengers_data = validated_data.pop('passengers', [])
        user = self.context['request'].user
        train = validated_data['train']

        reservation = Reservation.objects.create(
            user=user,
            train=train,
            quantity=validated_data['quantity']
        )

        for passenger_data in passengers_data:
            Passenger.objects.create(reservation=reservation, **passenger_data)

        return reservation
