from django.conf import settings
from django.db import models
import datetime
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from .constants import YES_NO_CHOICES, MEAT_CHOICES, COURSE_CHOICES, GENRE_CHOICES, RATING_CHOICES
from multiselectfield import MultiSelectField
from django.dispatch import receiver
from django.contrib.auth.models import User
from tinymce import models as tinymce_models

User = settings.AUTH_USER_MODEL

class Cooking(models.Model):
	user			= models.ForeignKey(User, on_delete=models.CASCADE)
	title			= models.CharField(max_length=100, blank=True, null=True)
	course			= models.CharField(max_length=100, choices=COURSE_CHOICES, null=True, blank=True)
	meat			= MultiSelectField(choices=MEAT_CHOICES, null=True, blank=True, default="None")
	URL_link		= models.URLField(max_length=500, blank=True, null=True)
	ingredients		= models.TextField(max_length=1000, blank=True, null=True)
	instructions	= models.TextField(max_length=1000, blank=True, null=True)
	tinymce_test	= models.TextField(max_length=1000, null=True, blank=True)
	# tinymce_test_2	= tinymce_models.HTMLField()

    # COMPLETION PROGRESS
	timestamp_added	= models.DateTimeField(auto_now_add=True)
	timestamp_updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-timestamp_added']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('hobbies:cooking_listview')


	# @property
	# def title(self):
	# 	return self.title

class Guitar(models.Model):
	user			= models.ForeignKey(User, on_delete=models.CASCADE)
	song       		= models.CharField(max_length=100, blank=True, null=True)
	artist     		= models.CharField(max_length=100, blank=True, null=True)
	tab				= models.TextField(max_length=1000, blank=True, null=True)
	url_lyrics		= models.URLField(max_length=1000, blank=True, null=True)
	url_link_1		= models.URLField(max_length=1000, blank=True, null=True)
	url_link_2		= models.URLField(max_length=1000, blank=True, null=True)
	file_1			= models.FileField(upload_to="guitar/", max_length=100, blank=True, null=True, default="None")
	file_2			= models.FileField(upload_to="guitar/", max_length=100, blank=True, null=True, default="None")
	rating			= models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
	genre			= models.CharField(max_length=100, choices=GENRE_CHOICES, blank=True, null=True)
	my_set			= models.BooleanField(default=False)

	# COMPLETION PROGRESS
	timestamp_added	= models.DateTimeField(auto_now_add=True)
	timestamp_updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-timestamp_added']

	def __str__(self):
		return self.item

	def get_absolute_url(self):
		return reverse('hobbies:guitar_listview')

	# @property
	# def title(self):
	# 	return self.task
