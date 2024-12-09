from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True, 
        validators = [UniqueValidator(queryset=User.objects.all())],
        error_messages={
            "unique": "A user with that email already exists.",
        },
        )
    confirm_password = serializers.CharField(max_length = 128, required = True, write_only = True)

    class Meta:
        model = User
        fields = (
            "username", "email", "password", "confirm_password",
            "first_name", "last_name"
            )
        extra_kwargs = {
            "first_name":{"required":False},
            "last_name":{"required":False}
        }

    def validate(self, attrs):
        if attrs["password"]!=attrs["confirm_password"]:
            raise serializers.ValidationError({
                "password": "passwords must be match."
            })
        return super().validate(attrs)
    
    def create(self, validated_data):
        del validated_data["confirm_password"]
        return User.objects.create_user(**validated_data)