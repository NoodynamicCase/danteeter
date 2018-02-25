from django.conf import settings
from django.db import models
import datetime
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from .constants import CONNECTION_CHOICES, CONNECTION_QUALITY_CHOICES, YES_NO_CHOICES
from multiselectfield import MultiSelectField
from django.dispatch import receiver
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL

class Contacts(models.Model):
	user			= models.ForeignKey(User, on_delete=models.CASCADE)
    # CONTACT INFO
	first_name		= models.CharField(max_length=75, blank=True, null=True)
	last_name       = models.CharField(max_length=75, blank=True, null=True)
	email           = models.EmailField(max_length=200, blank=True, null=True)
	phone           = models.CharField(max_length=13, blank=True, null=True)
	quick_reference = models.CharField(max_length=100, blank=True, null=True)
	notes     		= models.TextField(max_length=1000, blank=True, null=True)
	new       		= models.BooleanField(default=True)

    # CONNECTION TYPE
	connection_type     = MultiSelectField(choices=CONNECTION_CHOICES, null=True, blank=True)
	connection_quality 	= MultiSelectField(choices=CONNECTION_QUALITY_CHOICES, null=True, blank=True)
	file_upload		 	= models.FileField(upload_to="contacts/%Y/%M/", max_length=100, blank=True, null=True, default="None")

	# OTHER
	last_contacted  = models.DateField(max_length=100, blank=True, null=True)
	timestamp_added	= models.DateTimeField(auto_now_add=True)
	timestamp_updated = models.DateTimeField(auto_now=True)

    # PERSONAL INFO
	# LinkedIn
	# Facebook
	# Other email addresses
	# Other phone numbers

	# gender          = models.CharField(max_length = 10, choices=GENDER_CHOICES, blank=True, null=True)
	# age             = models.IntegerField(blank=True, null=True)
	# hometown        = models.TextField(max_length = 100, blank=True, null=True)
	# jobs            = models.TextField(max_length = 200, blank=True, null=True)
	# school          = models.TextField(max_length = 100, blank=True, null=True)
	# significant_other  = models.CharField(max_length = 100, blank=True, null=True)
	# children        = models.CharField(max_length = 200, blank=True, null=True)
	# hobbies         = models.TextField(max_length = 200, blank=True, null=True)
	# extra_bio_info  = models.TextField(max_length=1000, blank=True, null=True)
	# birthday        = models.DateField(blank=True, null=True)

	class Meta:
		ordering = ['-timestamp_added']

	def __str__(self):
		return self.last_name

	def get_absolute_url(self):
		return reverse('contacts:listview')

	@property
	def title(self):
		return self.last_name

# def forum_pre_save_receiver(sender, instance, *args, **kwargs):
    # instance.category = instance.category.capitalize()
    # if not instance.slug:
    #     instance.slug = unique_slug_generator(instance)

# pre_save.connect(forum_pre_save_receiver, sender=ForumPost)
