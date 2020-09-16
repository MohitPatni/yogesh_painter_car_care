from django.db import models


class MasterService(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0)


class Service(models.Model):
    master_service = models.ForeignKey(
        MasterService, on_delete=models.CASCADE )
    tital = models.CharField(max_length=100)
    service_name = models.CharField(max_length=100)
    desc = models.TextField()
    image_file =models.ImageField(upload_to='myphoto/%Y/%m/%d/', null=True, max_length=255)
    is_public_image = models.IntegerField(default=0)
    particular_work = models.JSONField( null=True)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0)


class PhotoGallary(models.Model):
    master_service = models.ForeignKey(
        MasterService, on_delete=models.CASCADE)
    tital = models.CharField(max_length=100)
    image_file = models.ImageField(upload_to='myphoto/%Y/%m/%d/', null=True, max_length=255)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0)


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=11)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0)


class ServiceEnquiy(models.Model):
    enquiry = models.ForeignKey(
        Enquiry, on_delete=models.CASCADE )
    Service = models.ForeignKey(
        Service, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0)


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    desc = models.TextField()
    rating = models.IntegerField()
    is_show = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0)


class Offer(models.Model):
    file_image = models.FileField(blank=False, null=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    offer_percent = models.IntegerField(3)
    tital = models.CharField(max_length=100)
    desc = models.TextField(null=True)
    is_active = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=11)
    alternative_number = models.CharField(max_length=11, null=True)
    address = models.TextField()
    other_info = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0)


class JobCard(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)
    offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=100)
    date_recived = models.DateTimeField(auto_now_add=True)
    registration_number = models.CharField(max_length=50)
    color = models.CharField(max_length=25)
    receiving_km = models.IntegerField()
    additional_discount = models.IntegerField()
    deposit = models.IntegerField()
    extra_work_price = models.IntegerField(null=True)
    extra_work_desc = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0)

class Work(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE)
    job_card = models.ForeignKey(
        JobCard, on_delete=models.CASCADE)
    job_card_work = models.JSONField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0)

class Billing(models.Model):
    job_card = models.ForeignKey(
        JobCard, on_delete=models.CASCADE)
    discount = models.IntegerField() 
    total = models.IntegerField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0)


class UserIPAddress(models.Model):
    ip_address = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0)




