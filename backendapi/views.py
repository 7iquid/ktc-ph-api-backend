from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

import requests
from DtcModels.models import Photo
from .serializer import PhotoSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Create your views here.

# @api_view(['GET','POST'])
class  MainApiView(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	# renderer_classes = [JSONRenderer]
	# renderer_classes = [TemplateHTMLRenderer]
	# item = Photo.objects.all()
	# serializer = PhotoSerializer(item, many=True)
	# return Response(serializer.data) 

	def get(self, request, format=None):
		content = {
		'user': str(request.user),  # `django.contrib.auth.User` instance.
		'auth': str(request.auth),  # None
		}
		# serializer = PhotoSerializer(item, many=True)
		return Response({'name':'tamina'})


@api_view(['GET','POST'])
def getData(request):
	item = Photo.objects.all()
	serializer = PhotoSerializer(item, many=True)
	return Response(serializer.data) 


@api_view(['POST'])
def addItem(request):
	serializer = PhotoSerializer(data =request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
	