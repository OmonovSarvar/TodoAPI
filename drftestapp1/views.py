from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import TodoModel
from .serializers import TodoSerializer


# Create your views here.

class TodoCreate(CreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer


class TodoList(ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer


class TodoUpdate(UpdateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'id'


class TodoDelete(DestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'id'


class TodoDetail(RetrieveAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'id'
