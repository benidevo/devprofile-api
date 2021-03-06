# Generated by Django 3.2.6 on 2021-09-05 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0004_alter_project_developer'),
    ]

    operations = [
        migrations.AddField(
            model_name='developerprofile',
            name='stack',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='developer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects', to='developer.developerprofile'),
        ),
    ]
