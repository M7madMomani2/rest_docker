from rest_app.models import Post
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import PostSerializers
# Create your views here.
class ListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class= PostSerializers

class DetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class= PostSerializers


    

