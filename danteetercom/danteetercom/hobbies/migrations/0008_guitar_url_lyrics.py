# Generated by Django 2.0.1 on 2018-01-27 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobbies', '0007_auto_20180126_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitar',
            name='url_lyrics',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
