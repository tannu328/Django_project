from urllib import response
from django.shortcuts import get_object_or_404, render
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from djangoapi_app.serializer import UserSerializer
from rest_framework import generics,filters
from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Usergenericview(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes=[IsAdminUser]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['email','first_name','last_name']
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['email','first_name','last_name']



    def list(self,request,*args,**kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # serializer= UserSerializer(queryset,many=True)
        # filter_backends = [DjangoFilterBackend]
        # filterset_fields = ['email']
        # user_input=email|first_name|last_name
        email = request.query_params.get('email')
        first_name= request.query_params.get('first_name')
        last_name = request.query_params.get('last_name')
        search= request.query_params.get(email or first_name or last_name)

        if  search:
            queryset = queryset.filter(search=search)

        serializer = UserSerializer(queryset, many=True)
        return Response({"data": serializer.data})
            # serializer = UserSerializer(queryset, many=True)
        # return Response({"data": serializer.data})
    
        # if first_name:
        #     queryset = queryset.filter(first_name=first_name)
        #     # serializer = UserSerializer(queryset, many=True)

        # if last_name:
        #     queryset = queryset.filter(last_name=last_name)
        

    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created!", "data": serializer.data})
        else:
            return Response(serializer.errors)
    
    def put(self,request,id):
        user=get_object_or_404(User,id=id)
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"update","data":serializer.data},status=200)
        else:
            # print("Request Data:request.data")
            # print("Serializer Errors:", serializer.errors)
            return Response({"error":serializer.errors},status=400)
    
    def patch(self,request,id):
        user=get_object_or_404(User,id=id)
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"update","data":serializer.data},status=200)
        else:
            # print("Request Data:request.data")
            # print("Serializer Errors:", serializer.errors)
            return Response(serializer.errors,status=400)
        
    def delete(self, request, id):
        user = get_object_or_404(User, id=id)
        user.delete()
        return Response({"message": "User deleted successfully"}, status=200)

        
 
class USerlogin(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[AllowAny]

    def post(self,request,*args,**kwargs):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username,password=password)

        if user!=None:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                serializer = UserSerializer(user)
                queryset=self.get_queryset()
                serializers=UserSerializer(queryset,many=True)  
                return Response({"message": "login success","access_token": access_token,"refresh_token": str(refresh)},status=200)
        else:
                return Response({"error":"invalide username and password"},status=400)



