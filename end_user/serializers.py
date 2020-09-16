from rest_framework import  serializers
from end_user import models

class MasterServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.MasterService
        fields='__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Feedback
        fields='__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Service
        fields='__all__'

class PhotoGallarySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.PhotoGallary
        fields='__all__'


