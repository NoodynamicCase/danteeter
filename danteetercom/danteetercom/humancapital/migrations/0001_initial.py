# Generated by Django 2.0.1 on 2018-01-19 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HumanCapitalJargon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_or_phrase', models.CharField(blank=True, max_length=100, null=True)),
                ('relates_to', models.CharField(blank=True, choices=[('Change Mgmt + Communications', 'Change Mgmt + Communications'), ('Leadership + Management', 'Leadership + Management'), ('Org Design', 'Org Design'), ('Culture', 'Culture'), ('Talent Acquisition', 'Talent Acquisition'), ('Talent Mgmt + Retention', 'Talent Mgmt + Retention'), ('Performance Management', 'Performance Management'), ('Pay & Benefits', 'Pay & Benefits'), ('Learning & Development', 'Learning & Development'), ('Training', 'Training'), ('HR Strategies + Services', 'HR Strategies + Services'), ('Tech Adoption', 'Tech Adoption'), ('Mergers & Acquisitions', 'Mergers & Acquisitions')], max_length=100, null=True)),
                ('definition', models.TextField(blank=True, max_length=500, null=True)),
                ('timestamp_added', models.DateTimeField(auto_now_add=True)),
                ('timestamp_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-word_or_phrase'],
            },
        ),
        migrations.CreateModel(
            name='HumanCapitalPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_topic', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Change Mgmt + Communications', 'Change Mgmt + Communications'), ('Leadership + Management', 'Leadership + Management'), ('Org Design', 'Org Design'), ('Culture', 'Culture'), ('Talent Acquisition', 'Talent Acquisition'), ('Talent Mgmt + Retention', 'Talent Mgmt + Retention'), ('Performance Management', 'Performance Management'), ('Pay & Benefits', 'Pay & Benefits'), ('Learning & Development', 'Learning & Development'), ('Training', 'Training'), ('HR Strategies + Services', 'HR Strategies + Services'), ('Tech Adoption', 'Tech Adoption'), ('Mergers & Acquisitions', 'Mergers & Acquisitions')], max_length=100, null=True)),
                ('post_title', models.CharField(blank=True, max_length=200, null=True)),
                ('post', models.TextField(blank=True, max_length=5000, null=True)),
                ('sources', models.TextField(blank=True, max_length=1000, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='humancapital/posts/%Y/')),
                ('complete', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True)),
                ('public_or_private', models.CharField(blank=True, choices=[('Private', 'Private'), ('Public', 'Public')], max_length=10, null=True)),
                ('timestamp_added', models.DateTimeField(auto_now_add=True)),
                ('timestamp_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp_added'],
            },
        ),
    ]
