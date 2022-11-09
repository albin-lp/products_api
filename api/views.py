from django.shortcuts import render
from api.models import Catagories,Products
from api.serializers import UserSerilazer,ProductSerilizer,CategorySerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import authentication,permissions
from rest_framework.decorators import action


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


class CategoryView(ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Catagories.objects.all()

#localhost:8000/categories/{id}/add_product
    @action(methods=["POST"],detail=True)
    def add_product(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        user=request.user
        cat=Catagories.objects.get(id=id)
        serilizer=ProductSerilizer(data=request.data,context={"category":cat,"user":user})
        if serilizer.is_valid():
            serilizer.save()
            return Response(data=serilizer.data)
        else:
            return Response(data=serilizer.errors)

#localhost:8000/categories/{id}/get_produts
    @action(methods=["GET"],detail=True)
    def get_product(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cat=Catagories.objects.get(id=id)
        prdt=cat.products_set.all()
        serializer=ProductSerilizer(prdt,many=True)
        return Response(serializer.data)

#
# class ProductView(ModelViewSet):
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     serializer_class = ProductSerilizer
#     queryset = Products.objects.all()

class ProductView(ViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

 # localhost:8000/products/{id}
    def list(self,request,*args,**kwargs):
        all_products=Products.objects.all()
        serilaizer=ProductSerilizer(all_products,many=True)
        return Response(data=serilaizer.data)

 # localhost:8000/products/{id}

    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        prdt=Products.objects.get(id=id)
        serializer=ProductSerilizer(prdt,many=False)
        return Response(data=serializer.data)

 # localhost:8000/products/{id}
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        instance=Products.objects.get(id=id)
        serializer=ProductSerilizer(instance=instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

 # localhost:8000/products/{id}
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        prdt=Products.objects.get(id=id)
        prdt.delete()
        return Response({"msg":"product deleted"})




















