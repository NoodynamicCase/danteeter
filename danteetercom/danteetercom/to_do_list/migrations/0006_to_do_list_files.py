# Generated by Django 2.0.1 on 2018-01-28 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0005_to_do_list_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='to_do_list',
            name='files',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='to_do_list.To_Do_List_File'),
        ),
    ]
