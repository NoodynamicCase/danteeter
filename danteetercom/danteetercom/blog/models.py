from django.conf import settings
from django.db import models
import datetime
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from .constants import YES_NO_CHOICES, PUBLIC_PRIVATE_CHOICES, POST_CATEGORY_CHOICES
from multiselectfield import MultiSelectField
from django.dispatch import receiver
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL

class Blog(models.Model):
	user			= models.ForeignKey(User, on_delete=models.CASCADE)
	post_category   = models.CharField(max_length=50, choices=POST_CATEGORY_CHOICES, null=True, blank=True, default="Daily Entry")
	post_title      = models.CharField(max_length=100, blank=True, null=True)
	post_entry      = models.TextField(max_length=10000, blank=True, null=True)
	public_private  = MultiSelectField(choices=PUBLIC_PRIVATE_CHOICES, null=True, blank=True, default="Private")
	timestamp_added	= models.DateTimeField(auto_now_add=True)
	timestamp_updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-timestamp_added']

	def __str__(self):
		return self.post_title

	def get_absolute_url(self):
		return reverse('blog:detailview', kwargs={'pk' : self.pk})

	@property
	def title(self):
		return self.post_title
