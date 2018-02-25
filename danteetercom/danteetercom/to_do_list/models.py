from django.conf import settings
from django.db import models
import datetime
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from .constants import YES_NO_CHOICES, URGENCY_CHOICES, IMPORTANCE_CHOICES, TASK_CATEGORY_CHOICES, GOOD_BODY_HABIT_CHOICES, GOOD_MENTAL_HABIT_CHOICES, GOOD_EFFICIENCY_HABIT_CHOICES
from multiselectfield import MultiSelectField
from django.dispatch import receiver
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL

class To_Do_List(models.Model):
	user			= models.ForeignKey(User, on_delete=models.CASCADE)
	task       		= models.CharField(max_length=100, blank=True, null=True)
	task_specifics  = models.TextField(max_length=1000, blank=True, null=True)
	task_urgency    = models.CharField(max_length=50, choices=URGENCY_CHOICES, null=True, blank=True, default="(not specified)")
	task_importance = models.CharField(max_length=50, choices=IMPORTANCE_CHOICES, null=True, blank=True, default="(not specified)")
	task_category  	= models.CharField(max_length=50, choices=TASK_CATEGORY_CHOICES, null=True, blank=True, default="(not specified)")
	files			= models.ForeignKey('To_Do_List_File', on_delete=models.CASCADE, blank=True, null=True)

    # COMPLETION PROGRESS
	task_followup	      	= models.BooleanField(default=False)
	task_completed      	= models.BooleanField(default=False)
	task_archive			= models.BooleanField(default=False)
	timestamp_added	= models.DateTimeField(auto_now_add=True)
	timestamp_updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-timestamp_added']

	def __str__(self):
		return self.task

	def get_absolute_url(self):
		return reverse('to_do_list:tasks_listview')

	@property
	def title(self):
		return self.task

class To_Do_List_File(models.Model):
	user			= models.ForeignKey(User, on_delete=models.CASCADE)
	name			= models.CharField(max_length=100, blank=True, null=True)
	uploaded_file	= models.FileField(upload_to="to_do_list/%Y/%M/", max_length=100, blank=True, null=True, default="None")
	timestamp_added	= models.DateTimeField(auto_now_add=True)
	timestamp_updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-timestamp_added']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('to_do_list:tasks_listview')

	@property
	def title(self):
		return self.uploaded_file

# ====== DAILY GRIND ===========================================================
class DailyLog(models.Model):
	user			= models.ForeignKey(User, on_delete=models.CASCADE)
	entry_title		= models.CharField(max_length=100, blank=True, null=True)
	entry			= models.TextField(max_length=500, blank=True, null=True)
	good_body_habits	= MultiSelectField(choices=GOOD_BODY_HABIT_CHOICES, blank=True, null=True)
	good_mental_habits	= MultiSelectField(choices=GOOD_MENTAL_HABIT_CHOICES , blank=True, null=True)
	good_efficiency_habits	= MultiSelectField(choices=GOOD_EFFICIENCY_HABIT_CHOICES , blank=True, null=True)

	timestamp_added	= models.DateTimeField(auto_now_add=True)
	timestamp_updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-timestamp_added']

	def __str__(self):
		return self.entry_title

	def get_absolute_url(self):
		return reverse('to_do_list:dailylog_listview')

	@property
	def title(self):
		return self.timestamp_added
