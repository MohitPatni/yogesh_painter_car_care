# Generated by Django 3.1.1 on 2020-10-16 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('end_user', '0004_delete_myphoto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServiceEnquiy',
            new_name='ServiceEnquiry',
        ),
        migrations.AlterField(
            model_name='photogallary',
            name='image_file',
            field=models.ImageField(max_length=255, null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image_file',
            field=models.ImageField(max_length=255, null=True, upload_to='img'),
        ),
    ]
