# Generated by Django 2.0.1 on 2018-02-02 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0010_shopping_stores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='follow_up',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='max_spend',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='repeat_item',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='stores',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='urgency',
        ),
        migrations.AddField(
            model_name='shopping',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='archive',
            field=models.BooleanField(default=False, verbose_name='Save and Archive'),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='recipient',
            field=models.CharField(blank=True, choices=[('Shared', 'Shared'), ('Dan', 'Dan'), ('Alice', 'Alice'), ('Other', 'Other')], default='Shared', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='store',
            field=models.CharField(blank=True, choices=[('Grocery', 'Grocery'), ('Other', 'Other')], default='Grocery', max_length=100, null=True),
        ),
    ]
