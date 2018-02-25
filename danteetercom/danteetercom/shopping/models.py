from django.conf import settings
from django.db import models
import datetime
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from .constants import STORE_CATEGORY_CHOICES, ITEM_CATEGORY_CHOICES, RECIPIENT_CHOICES
from multiselectfield import MultiSelectField
from django.dispatch import receiver
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL

class Shopping(models.Model):
	user			= models.ForeignKey(User, on_delete=models.CASCADE)

	# ITEM INFO
	item       		= models.CharField(max_length=100, blank=True, null=True)
	specifics       = models.TextField(max_length=1000, blank=True, null=True)
	store			= models.CharField(max_length=100, choices=STORE_CATEGORY_CHOICES, null=True, blank=True, default="Grocery")
	item_category	= models.CharField(max_length=50, choices=ITEM_CATEGORY_CHOICES, null=True, blank=True, default="Food")
	recipient		= models.CharField(max_length=50, choices=RECIPIENT_CHOICES, null=True, blank=True, default="Shared")

	# OTHER INFO
	item_url		= models.URLField(max_length=500, blank=True, null=True)
	picture         = models.ImageField(upload_to='uploads/%Y/%m/', null=True, blank=True)

	# COMPLETION PROGRESS
	wish_list		= models.BooleanField(default=False)
	ordered			= models.BooleanField(default=False)
	favorite		= models.BooleanField(default=False)
	in_list      	= models.BooleanField(default=True, verbose_name = "In List?")
	timestamp_added	= models.DateTimeField(auto_now_add=True)
	timestamp_updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-timestamp_added']

	def __str__(self):
		return self.item

	def get_absolute_url(self):
		return reverse('shopping:listview')

	@property
	def title(self):
		return self.item
