# Generated by Django 3.2.6 on 2021-09-06 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiterprofile',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='recruiter/profile'),
        ),
    ]
