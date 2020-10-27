from django.shortcuts import render, HttpResponse
from rest_framework import generics
from end_user import serializers, models, utils
from end_user.models import MasterService
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status


class FeedbackAPIView(APIView):
    def get(self, request, *args, **kwargs):
        fields = ('name', 'desc', 'rating')
        qs = models.Feedback.objects.filter(
            is_deleted__exact=0).filter(is_show__exact=0)
        feedback_serializer = serializers.FeedbackSerializer(
            qs, many=True, fields=fields)
        if feedback_serializer.data:
            return Response({'data': feedback_serializer.data, 'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': " No Data found"}, status=404)

    def post(self, request, *args, format=None, **kwargs):

        feedback_serializer = serializers.FeedbackSerializer(data=request.data)
        if feedback_serializer.is_valid():
            feedback_serializer.save()
            return Response({'message': 'Feedback Send', 'status': 'success'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Something went wrong', 'status': 'error', 'error': feedback_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ServiceAPIView(APIView):
    def get(self, request, *args, **kwargs):
        fields = ('id', 'service_name')
        qs = models.Service.objects.filter(is_deleted__exact=0)
        service_serializer = serializers.ServiceSerializer(qs, many=True,fields=fields)
        if service_serializer.data:
            return Response({'data': service_serializer.data, 'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': " No Data found"}, status=404)


class ContactAPIView(APIView):
    def post(self, request, *args, format=None, **kwargs):
        enquiry_serializer = serializers.EnquirySerializer(data=request.data)
        if enquiry_serializer.is_valid():
            enquiry_serializer.save()
            return Response({'message': 'Message Send', 'status': 'success'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Something went wrong', 'status': 'error', 'error': enquiry_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        qs = models.Enquiry.objects.filter(is_deleted__exact=0)
        enquiry_serializer = serializers.EnquirySerializer(qs, many=True)
        if enquiry_serializer.data:
            return Response({'data': enquiry_serializer.data, 'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': " No Data found"}, status=404)


class MasterServiceAPIView(APIView):
    def get(self, request, *args, **kwargs):
        fields = ('id', 'name')
        qs = models.MasterService.objects.filter(is_deleted__exact=0)
        master_serializer= serializers.MasterServiceSerializer(qs, many=True,fields=fields)
        if master_serializer.data:
            return Response({'data': master_serializer.data, 'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': " No Data found"}, status=404)


class TestServiceAPIView(APIView):
     def get(self, request,pk, *args, **kwargs):
       print(pk)
       return Response({'data': pk, 'status': 'success'}, status=status.HTTP_200_OK)


# class MasterServiceRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
#     serializer_class = serializers.MasterServiceSerializer

#     def get_queryset(self):
#         qs = MasterService.objects.all()
#         qs = qs.filter(is_deleted__exact=0)
#         return qs


# class MasterServiceRetriveAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         qs = models.MasterService.objects.filter(is_deleted__exact=0)
#         serializer = serializers.MasterServiceSerializer(qs, many=True)
#         if serializer.data:

#             return Response({'data': serializer.data, 'status': 'success'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': " No Data found"}, status=404)


# class FeedbackListCreateAPIView(generics.ListCreateAPIView):

#     serializer_class = serializers.FeedbackSerializer

#     def get_queryset(self):
#         qs = models.Feedback.objects.all()
#         qs = qs.filter(is_deleted__exact=0)
#         return qs


# class FeedbackRetriveForShow(APIView):
#     def get(self, request, *args, **kwargs):
#         qs = models.Feedback.objects.filter(
#             is_deleted__exact=0).filter(is_show__exact=0)
#         serializer = serializers.FeedbackSerializer(qs, many=True)
#         if serializer.data:

#             return Response({'data': serializer.data, 'status': 'success'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': " No Data found"}, status=404)


# class FeedbackRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
#     serializer_class = serializers.FeedbackSerializer

#     def get_queryset(self):
#         qs = models.Feedback.objects.all()
#         qs = qs.filter(is_deleted__exact=0)
#         return qs


# class CreateServiceRetriveBYMasterIDServiceAPIView(APIView):
#     def post(self, request, *args, format=None, **kwargs):
#         service_serializer = serializers.ServiceSerializer(data=request.data)
#         if service_serializer.is_valid():
#             service_serializer.save()
#             return Response(service_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, *args, **kwargs):
#         master_service_id = self.request.query_params.get('my-service')
#         qs = models.Service.objects.filter(is_deleted__exact=0).filter(
#             master_service_id__exact=master_service_id)
#         serializer = serializers.ServiceSerializer(qs, many=True)
#         if serializer.data:
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response("No Data found", status=404)


# class ServiceListAPIView(generics.ListAPIView):
#     serializer_class = serializers.ServiceSerializer

#     def get_queryset(self):
#         qs = models.Service.objects.all()
#         qs = qs.filter(is_deleted__exact=0)
#         return qs


# class ServiceRetrieveUpdateByIDAPIView(generics.RetrieveUpdateAPIView):
#     serializer_class = serializers.ServiceSerializer

#     def get_queryset(self):
#         qs = models.Service.objects.all()
#         qs = qs.filter(is_deleted__exact=0)
#         return qs


# class CreatePhotoGallaryRetriveBYMasterIDServiceAPIView(APIView):
#     def post(self, request, *args, format=None, **kwargs):
#         photo_gallary_serializer = serializers.PhotoGallarySerializer(
#             data=request.data)
#         if photo_gallary_serializer.is_valid():
#             photo_gallary_serializer.save()
#             return Response(photo_gallary_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(photo_gallary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, *args, **kwargs):
#         master_service_id = self.request.query_params.get('get-photo')
#         qs = models.PhotoGallary.objects.filter(is_deleted__exact=0).filter(
#             master_service_id__exact=master_service_id)
#         serializer = serializers.PhotoGallarySerializer(qs, many=True)
#         if serializer.data:
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response("No Data found", status=404)
