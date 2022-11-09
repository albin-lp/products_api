from api.models  import Catagories,Products
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerilazer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class CategorySerializer(serializers.ModelSerializer):
    is_active=serializers.BooleanField(read_only=True)
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Catagories
        fields=["catagory_name","is_active","id"]
class  CatagoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Catagories
        fields=["catagory_name"]



class ProductSerilizer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    cat=CatagoryNameSerializer(many=False,read_only=True)
    class Meta:
        model=Products
        fields="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        cat=self.context.get("category")
        return Products.objects.create(**validated_data,user=user,cat=cat)



