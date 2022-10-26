from api.models import Products
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerilazer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ProductSerilizer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Products
        fields="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        return Products.objects.create(**validated_data,user=user)



