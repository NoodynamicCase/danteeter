from django.conf import settings
from django.db import models
import datetime
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from .constants import YES_NO_CHOICES, TASK_CATEGORY_CHOICES
from multiselectfield import MultiSelectField
from django.dispatch import receiver
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL

class Timer(models.Model):
	user			= models.ForeignKey(User, on_delete=models.CASCADE)
	task_category	= models.CharField(max_length=100, choices=TASK_CATEGORY_CHOICES, blank=True, null=True)
	start_time		= models.DateTimeField(auto_now_add=True)
	stop_time		= models.DateTimeField(auto_now=True)
	total_time		= models.CharField(max_length=20, blank=True, null=True)
	task_description = models.TextField(max_length=300, blank=True, null=True)

	class Meta:
		ordering = ['-stop_time']

	def __str__(self):
		return self.task_description

	def get_absolute_url(self):
		return reverse('timer:listview')
		# return reverse('timer:updateview', kwargs={'pk' : self.id})

	@property
	def title(self):
		return self.task_description
