from rest_framework import  serializers
from end_user import models
class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class MasterServiceSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model=models.MasterService
        fields='__all__'

class FeedbackSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model=models.Feedback
        fields='__all__'



class ServiceSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model=models.Service
        fields='__all__'

class ServiceEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ServiceEnquiry
        fields = ('id', 'Service')

class EnquirySerializer(serializers.ModelSerializer):
   
    service_enquiry = ServiceEnquirySerializer( many=True)
    class Meta:
        model=models.Enquiry
        fields = ('id',  'name', 'contact_number','email','message','service_enquiry')

    def create(self, validated_data):
        service_enquiry = validated_data.pop('service_enquiry')
        enquiry = models.Enquiry.objects.create(**validated_data)
        for data in service_enquiry:
            models.ServiceEnquiry.objects.create(enquiry=enquiry, **data)
        return enquiry



class PhotoGallarySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.PhotoGallary
        fields='__all__'


