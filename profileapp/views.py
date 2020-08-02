from django.shortcuts import render
from rest_framework.decorators import  APIView
# Create your views here.
from .models import Profile
from .serializers import ProfileSerializer
from django.http  import HttpResponse

class ProfileView (APIView):

    def get(self, request):
        profiles= Profile.objects.all ()
        if profiles:
            serializer = ProfileSerializer(profiles, many=True)
            #if (serializer.is_valid()):
            return HttpResponse(serializer.data)
        else :
            return HttpResponse('none')


    def post (self):
        pass