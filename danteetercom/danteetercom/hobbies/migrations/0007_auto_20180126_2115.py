# Generated by Django 2.0.1 on 2018-01-27 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobbies', '0006_auto_20180122_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guitar',
            name='task_completed',
        ),
        migrations.AddField(
            model_name='guitar',
            name='artist',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='guitar',
            name='file_1',
            field=models.FileField(blank=True, default='None', null=True, upload_to='guitar/'),
        ),
        migrations.AddField(
            model_name='guitar',
            name='file_2',
            field=models.FileField(blank=True, default='None', null=True, upload_to='guitar/'),
        ),
        migrations.AddField(
            model_name='guitar',
            name='genre',
            field=models.CharField(blank=True, choices=[('Classic Rock', 'Classic Rock'), ('Alternative', 'Alternative'), ('Grunge', 'Grunge'), ('Other', 'Other')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='guitar',
            name='my_set',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='guitar',
            name='rating',
            field=models.IntegerField(blank=True, choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], null=True),
        ),
        migrations.AddField(
            model_name='guitar',
            name='song',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='guitar',
            name='tab',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='guitar',
            name='url_link_1',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='guitar',
            name='url_link_2',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]