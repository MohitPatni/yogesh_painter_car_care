from django.shortcuts import render, HttpResponse
from rest_framework import generics
from end_user import serializers, models, utils
from end_user.models import MasterService
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status


class MasterServiceListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = serializers.MasterServiceSerializer

    def get_queryset(self):
        qs = MasterService.objects.all()
        qs = qs.filter(is_deleted__exact=0)
        return qs


class MasterServiceRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.MasterServiceSerializer
    def get_queryset(self):
        qs = MasterService.objects.all()
        qs = qs.filter(is_deleted__exact=0)
        return qs


class FeedbackListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = serializers.FeedbackSerializer
    def get_queryset(self):
        qs = models.Feedback.objects.all()
        qs = qs.filter(is_deleted__exact=0)
        return qs


class FeedbackRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.FeedbackSerializer
    def get_queryset(self):
        qs = models.Feedback.objects.all()
        qs=qs.filter(is_deleted__exact=0)
        return qs

class CreateServiceRetriveBYMasterIDServiceAPIView(APIView):
    def post(self, request, *args, format=None,**kwargs):
        service_serializer = serializers.ServiceSerializer(data=request.data)
        if service_serializer.is_valid():
          service_serializer.save()
          return Response(service_serializer.data, status=status.HTTP_201_CREATED)
        else:
          return Response(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args,**kwargs):
       master_service_id =  self.request.query_params.get('my-service')
       qs=models.Service.objects.filter(is_deleted__exact=0).filter(master_service_id__exact=master_service_id)
       serializer=serializers.ServiceSerializer(qs,many=True)
       if serializer.data:
         return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
         return Response("No Data found", status=404)  


class ServiceListAPIView(generics.ListAPIView):
    serializer_class = serializers.ServiceSerializer
    def get_queryset(self):
        qs = models.Service.objects.all()
        qs=qs.filter(is_deleted__exact=0)
        return qs

class ServiceRetrieveUpdateByIDAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.ServiceSerializer
    def get_queryset(self):
        qs = models.Service.objects.all()
        qs=qs.filter(is_deleted__exact=0)
        return qs


class CreatePhotoGallaryRetriveBYMasterIDServiceAPIView(APIView):
    def post(self, request, *args, format=None,**kwargs):
        photo_gallary_serializer = serializers.PhotoGallarySerializer(data=request.data)
        if photo_gallary_serializer.is_valid():
          photo_gallary_serializer.save()
          return Response(photo_gallary_serializer.data, status=status.HTTP_201_CREATED)
        else:
          return Response(photo_gallary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args,**kwargs):
       master_service_id =  self.request.query_params.get('get-photo')
       qs=models.PhotoGallary.objects.filter(is_deleted__exact=0).filter(master_service_id__exact=master_service_id)
       serializer=serializers.PhotoGallarySerializer(qs,many=True)
       if serializer.data:
         return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
         return Response("No Data found", status=404)  


