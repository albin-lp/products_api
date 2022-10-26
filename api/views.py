from django.shortcuts import render
from api.models import Products
from api.serializers import UserSerilazer,ProductSerilizer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import authentication,permissions


# Create your views here.
#localhost:8000/user/signup/
class UsersignupView(ViewSet):
    def create(self,request,*args,**kwargs):
        serilizer=UserSerilazer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(data=serilizer.data)
        else:
            return Response(data=serilizer.errors)

# localhost:8000/products
class ProductView(ViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def create(self,request,*args,**kwargs):
        user=request.user
        serializer=ProductSerilizer(data=request.data,context={"user":user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


# localhost:8000/products/
    def list(self,request,*args,**kwargs):
        all_products=Products.objects.all()
        serilaizer=ProductSerilizer(all_products, many=True)
        return Response(data=serilaizer.data)

 #localhost:8000/products/{id}
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        prdt=Products.objects.get(id=id)
        serializer=ProductSerilizer(prdt,many=False)
        return Response(data=serializer.data)

 # localhost:8000/products/{id}
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        prdct=Products.objects.get(id=id)
        prdct.delete()
        return Response(data={"msg":"product deleted"})

# localhost:8000/products/{id}
    def update(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        instance=Products.objects.get(id=id)
        serializer=ProductSerilizer(instance=instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)














