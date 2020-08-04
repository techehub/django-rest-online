from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .seralizer import TaskSerializer
from .models import Task

class TaskView (ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
