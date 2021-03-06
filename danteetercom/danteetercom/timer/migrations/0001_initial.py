# Generated by Django 2.0.1 on 2018-01-23 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_category', models.CharField(blank=True, choices=[('Client', 'Client'), ('PRD', 'PRD'), ('Travel', 'Travel'), ('Navy Reserves', 'Navy Reserves'), ('Personal', 'Personal')], max_length=100, null=True)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('stop_time', models.DateTimeField(auto_now=True)),
                ('total_time', models.CharField(blank=True, max_length=20, null=True)),
                ('task_description', models.TextField(blank=True, max_length=300, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-stop_time'],
            },
        ),
    ]
