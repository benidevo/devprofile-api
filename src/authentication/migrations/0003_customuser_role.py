# Generated by Django 3.2.6 on 2021-08-29 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_customuser_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(default='developer', max_length=50),
        ),
    ]