from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .seralizer import TaskSerializer
from .models import Task
from rest_framework.response import  Response

class TaskView (ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def list(self, request):
        name = request.GET.get ('name')
        if name:
            data= Task.objects.filter (name__contains = name)
        else:
            data = Task.objects.all ()

        ser = TaskSerializer(data, many=True)
        return Response (ser.data)