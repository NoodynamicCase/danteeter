# Generated by Django 2.0.1 on 2018-01-31 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('to_do_list', '0008_daily_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_title', models.CharField(blank=True, max_length=100, null=True)),
                ('entry', models.TextField(blank=True, max_length=500, null=True)),
                ('good_body_habits', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Stretched (5-min)', 'Stretched (5-min)'), ('Pushups', 'Pushups'), ('Situps', 'Situps'), ('Ran', 'Ran'), ('Healthy Breakfast', 'Healthy Breakfast'), ('Healthy Lunch', 'Healthy Lunch'), ('Healthy Dinner', 'Healthy Dinner'), ('Salad', 'Salad'), ('Low Meat Intake', 'Low Meat Intake'), ('No Alcohol', 'No Alcohol'), ('No Dessert', 'No Dessert'), ('No M', 'No M'), ('Bed before 10pm', 'Bed before 10pm')], max_length=148, null=True)),
                ('good_mental_habits', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Meditated (15-min)', 'Meditate (15-min)'), ('Relaxing Walk', 'Relaxing Walk'), ('Read for 30-min', 'Read for 30-min'), ('Spanish (15-min)', 'Spanish (15-min)'), ('Coding (30-min)', 'Coding (30-min)')], max_length=81, null=True)),
                ('good_efficiency_habits', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Morning Review', 'Morning Review'), ('Post-Lunch Update', 'Post-Lunch Update'), ('Post-Work Update', 'Post-Work Update'), ('Pre-bed Review', 'Pre-bed Review'), ('Tackled Hardest First', 'Tackled Hardest First'), ('Email Check 2x/hr', 'Email Check 2x/hr'), ('Computer off at 9pm', 'Computer Off at 9pm')], max_length=124, null=True)),
                ('timestamp_added', models.DateTimeField(auto_now_add=True)),
                ('timestamp_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp_added'],
            },
        ),
        migrations.RemoveField(
            model_name='daily_log',
            name='user',
        ),
        migrations.DeleteModel(
            name='Daily_Log',
        ),
    ]