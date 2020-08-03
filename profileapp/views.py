from django.shortcuts import render
from rest_framework.decorators import  APIView
# Create your views here.
from .models import Profile
from .serializers import ProfileSerializer
from  rest_framework.response  import Response

class InvalidProfileErr(Exception):
    pass

class ProfileDetailView (APIView):

    def getdata (self, id):
        try:
            profile = Profile.objects.get (id=  id)
        except:
            raise InvalidProfileErr ( )

    def get (self, req, id):
        try:
            profile =self.getdata(id)
            serializer = ProfileSerializer( profile)
            return Response(serializer.data)
        except InvalidProfileErr as e:
            print (e)
            return Response("Invalid profile id")

    def put (self, req, id):

        try :
            profile = self.getdata(id)
            serializer = ProfileSerializer(profile, req.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except InvalidProfileErr as e:
            print(e)
            return Response("Invalid profile id")

    def delete (self, req, id):
        try:
            profile =self.getdata(id)
            profile.delete()
            return Response("deleted")
        except InvalidProfileErr as e:
            print(e)
            return Response("Invalid profile id")


class ProfileView (APIView):

    def get(self, request):
        profiles= Profile.objects.all ()
        if profiles:
            serializer = ProfileSerializer(profiles, many=True)
            return Response(serializer.data)
        else :
            return Response('none')


    def post (self, request):
        print (request.data)
        serializer = ProfileSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
