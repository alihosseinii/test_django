from rest_framework import serializers
from .models import UserInformation
from django.contrib.auth.hashers import make_password
import re

class SingupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = ["phone_number", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
            "phone_number": {"required": True}
        }
    

    def validate_phone_number(self, value):
        pattern = r'^09\d{9}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("شماره تلفن باید با 09 شروع شود و دقیقاً 11 رقم عددی باشد.")
        return value
    

    def validate(self, data):
        data['username'] = data['phone_number']
        return data

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        user = UserInformation.objects.create(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        try:
            user = UserInformation.objects.get(phone_number=data.get("phone_number"))
        except UserInformation.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials")
        
        if not user.check_password(data.get("password")):
            raise serializers.ValidationError("Invalid credentials")
        
        data["user"] = user
        return data

