# Generated by Django 2.0.1 on 2018-01-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0006_to_do_list_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='to_do_list_file',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]