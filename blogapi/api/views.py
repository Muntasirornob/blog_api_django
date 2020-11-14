from django.shortcuts import render
from .models import Post,Profile
from.serializers import blogserializer,profileserializer,UserRegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import create_user_account
from . import serializers
from rest_framework import viewsets,status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# Create your views here.
@api_view(['GET'])
def blogapi(request):
	post=Post.objects.all()
	s=blogserializer(post,many=True)
	return Response(s.data)

@api_view(['GET'])
def profilesapi(request):
	profile=Profile.objects.all()
	se=profileserializer(profile,many=True)
	return Response(se.data)

@api_view(['GET'])
def blogdetailapi(request,pk):
	post=Post.objects.get(pk=pk)
	s=blogserializer(post,many=False)
	return Response(s.data)

@api_view(['GET','POST'])
def blogpostapi(request):
	s=blogserializer(data=request.data)
	if s.is_valid():
		s.save()
	return Response(s.data)

@api_view(['GET','POST'])
def blogpostupdateapi(request,pk):
	post=Post.objects.get(pk=pk)
	s=blogserializer(instance=post,data=request.data)
	if s.is_valid():
		s.save()
	return Response(s.data)

@api_view(['DELETE'])
def blogdeleteapi(request,pk):
	post=Post.objects.get(pk=pk)
	post.delete()
	return Response("deleted")


@api_view(['POST'])
def register(request):
	serializer =UserRegisterSerializer(data=request.data)
	serializer.is_valid(raise_exception=True)
	user = create_user_account(**serializer.validated_data)
	token=Token.objects.get(user=user).key
	data['token']=token
	data = serializer.data

	return Response(data=data, status=status.HTTP_201_CREATED)