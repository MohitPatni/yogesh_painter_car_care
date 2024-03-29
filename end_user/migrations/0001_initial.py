# Generated by Django 3.1.1 on 2020-09-15 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=11)),
                ('alternative_number', models.CharField(max_length=11, null=True)),
                ('address', models.TextField()),
                ('other_info', models.TextField(null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('desc', models.TextField()),
                ('rating', models.IntegerField()),
                ('is_show', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='JobCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(max_length=100)),
                ('date_recived', models.DateTimeField(auto_now_add=True)),
                ('registration_number', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=25)),
                ('receiving_km', models.IntegerField()),
                ('additional_discount', models.IntegerField()),
                ('deposit', models.IntegerField()),
                ('extra_work_price', models.IntegerField(null=True)),
                ('extra_work_desc', models.TextField(null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='end_user.customer')),
            ],
        ),
        migrations.CreateModel(
            name='MasterService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_image', models.FileField(null=True, upload_to='')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
                ('offer_percent', models.IntegerField(verbose_name=3)),
                ('tital', models.CharField(max_length=100)),
                ('desc', models.TextField(null=True)),
                ('is_active', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tital', models.CharField(max_length=100)),
                ('service_name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('image_file', models.FileField(null=True, upload_to='')),
                ('is_public_image', models.IntegerField(default=0)),
                ('particular_work', models.JSONField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('master_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='end_user.masterservice')),
            ],
        ),
        migrations.CreateModel(
            name='UserIPAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_card_work', models.JSONField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('job_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='end_user.jobcard')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='end_user.service')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceEnquiy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('Service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='end_user.service')),
                ('enquiry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='end_user.enquiry')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoGallary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tital', models.CharField(max_length=100)),
                ('image_file', models.FileField(null=True, upload_to='')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('master_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='end_user.masterservice')),
            ],
        ),
        migrations.AddField(
            model_name='jobcard',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='end_user.offer'),
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField()),
                ('total', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('job_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='end_user.jobcard')),
            ],
        ),
    ]
