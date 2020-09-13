from django.contrib import admin
from end_user import models


class MasterServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date', 'updated_date', 'is_deleted')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'master_service', 'tital',
                    'service_name', 'desc', 'image_file', 'is_public_image', 'particular_work', 'created_date', 'updated_date', 'is_deleted')


class PhotoGallaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'master_service', 'tital', 'image_file',
                    'created_date', 'updated_date', 'is_deleted')


class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_number', 'email',
                    'message', 'created_date', 'updated_date', 'is_deleted')


class ServiceEnquiyAdmin(admin.ModelAdmin):
    list_display = ('id', 'enquiry', 'Service', 'created_date',
                    'updated_date', 'is_deleted')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'desc', 'rating',
                    'created_date', 'updated_date', 'is_deleted')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'tital', 'desc', 'file_image', 'start_date',
                    'end_date', 'offer_percent', 'is_active', 'created_date', 'updated_date', 'is_deleted')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_number', 'alternative_number', 'address', 'other_info',
                    'created_date', 'updated_date', 'is_deleted')


class JobCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'offer', 'vehicle_type',
                    'date_recived', 'registration_number', 'color', 'receiving_km', 
                    'additional_discount', 'deposit', 'extra_work_price', 'extra_work_desc',
                    'created_date', 'updated_date', 'is_deleted')

class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'job_card', 'job_card_work', 
                    'created_date', 'updated_date', 'is_deleted')

class BillingAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_card', 'discount', 'total', 
                    'created_date', 'updated_date', 'is_deleted')

admin.site.register(models.MasterService,MasterServiceAdmin)
admin.site.register(models.Service,ServiceAdmin)
admin.site.register(models.PhotoGallary,PhotoGallaryAdmin)
admin.site.register(models.Enquiry,EnquiryAdmin)
admin.site.register(models.ServiceEnquiy,ServiceEnquiyAdmin)
admin.site.register(models.Feedback,FeedbackAdmin)
admin.site.register(models.Offer,OfferAdmin)
admin.site.register(models.Customer,CustomerAdmin)
admin.site.register(models.JobCard,JobCardAdmin)
admin.site.register(models.Work,WorkAdmin)
admin.site.register(models.Billing,BillingAdmin)
