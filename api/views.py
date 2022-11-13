from pydoc import importfile
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from numpy import generic
from yaml import serialize
from base.models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import messages
from rest_framework import generics

# ////////////////////////////////////
#             1st method starts
# ////////////////////////////////////

# @csrf_exempt
# def index(request):
#     if request.method == 'GET':
#         blogs = blog.objects.all()
#         serializer= BlogSerial(blogs, many=True)
#         return JsonResponse(serializer.data, safe= False)
#     elif request.method == 'POST':
#         JSONData = JSONParser().parse(request)
#         serializer = BlogSerial(data = JSONData)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe = False)
#         else:
#             return JsonResponse(serializer.errors, safe=False)

# @csrf_exempt
# def detail(request, pk):
#     try:
#         blogs = blog.objects.get(pk=pk)
#     except blog.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer= BlogSerial(blogs)
#         return JsonResponse(serializer.data, safe= False)

#     elif request.method == 'DELETE':
#         blogs.delete()
#         return HttpResponse(status = status.HTTP_204_NO_CONTENT, safe = False)
#     elif request.method == 'PUT':
#         JSONData = JSONParser().parse(request)
#         serializer = BlogSerial(blogs, data = JSONData)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe = False)
#         else:
#             return JsonResponse(serializer.errors, safe=False)


# ////////////////////////////////////
#             2nd method starts
# ////////////////////////////////////

# @api_view(['GET', 'POST'])
# def index(request):
#     if request.method == 'GET':
#         blogs = blog.objects.all()
#         serializer = BlogSerial(blogs, many = True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = BlogSerial(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'DELETE', 'PUT'])
# def detail(request, pk):
#     try:
#         blogs = blog.objects.get(pk=pk)
#     except blog.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer= BlogSerial(blogs)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         blogs.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = BlogSerial(blogs, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)



# ////////////////////////////////////
#             3rd method starts
# ////////////////////////////////////

# class index(APIView):
#     def get(self, request):
#         blogs = blog.objects.all()
#         serializer= BlogSerial(blogs, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = BlogSerial(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# class detail(APIView):
#     def get_blog(request, pk):
#         try:
#             return blog.objects.get(pk=pk)
#         except blog.DoesNotExist:
#             return HttpResponse(status=404)

#     def get(self, request, pk): 
#         blogs = self.get_blog(pk)
#         serializer= BlogSerial(blogs)
#         return Response(serializer.data)
        
#     def delete(self, request, pk):
#         blogs = self.get_blog(pk)
#         blogs.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)

#     def put(self, request, pk):
#         blogs = self.get_blog(pk)
#         serializer = BlogSerial(blogs, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# ////////////////////////////////////
#             4th method starts (Generics)
# ////////////////////////////////////

class room(generics.ListAPIView, generics. CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerial

class detail(generics.RetrieveAPIView, generics. UpdateAPIView, generics.DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerial

