# Generated by Django 3.2.6 on 2021-09-04 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]