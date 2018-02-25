from django.conf import settings
from django.db import models
import datetime
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from .constants import YES_NO_CHOICES, HC_TOPIC_CHOICES, PROJECT_TYPE_CHOICES, HC_SERVICE_AREA_CHOICES, PUBLIC_OR_PRIVATE_CHOICES
from multiselectfield import MultiSelectField
from django.dispatch import receiver
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL

# ====== POST =====================================================================
class HumanCapitalPost(models.Model):
	user			= models.ForeignKey(User, on_delete=models.CASCADE)
	post_topic		= MultiSelectField(max_length=100, choices=HC_TOPIC_CHOICES, null=True, blank=True)
	post_title		= models.CharField(max_length=200, blank=True, null=True)
	post			= models.TextField(max_length=5000, blank=True, null=True)
	sources			= models.TextField(max_length=1000, blank=True, null=True)
	upload_file		= models.FileField(upload_to="humancapital/posts/%Y/", max_length=100, blank=True, null=True, default="None")
	complete		= models.CharField(max_length=5, choices=YES_NO_CHOICES, null=True, blank=True)
	public_or_private	= models.CharField(max_length=10, choices=PUBLIC_OR_PRIVATE_CHOICES, null=True)
	timestamp_added	= models.DateTimeField(auto_now_add=True)
	timestamp_updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-timestamp_added']

	def __str__(self):
		return self.post_title

	def get_absolute_url(self):
		return reverse('humancapital:posts_listview')

	@property
	def title(self):
		return self.name

# ====== JARGON =====================================================================
class HumanCapitalJargon(models.Model):
	user			= models.ForeignKey(User, on_delete=models.CASCADE)
	word_or_phrase	= models.CharField(max_length=100,blank=True, null=True, verbose_name='Term or Acronym')
	relates_to		= models.CharField(max_length=100, choices=HC_TOPIC_CHOICES, blank=True, null=True)
	definition		= models.TextField(max_length=500, blank=True, null=True)
	timestamp_added	= models.DateTimeField(auto_now_add=True)
	timestamp_updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-word_or_phrase']

	def __str__(self):
		return self.word_or_phrase

	def get_absolute_url(self):
		return reverse('humancapital:jargon_listview')

	@property
	def title(self):
		return self.word_or_phrase


# ==== SOURCES =====================================================================
class HumanCapitalSource(models.Model):
	user			= models.ForeignKey(User, on_delete=models.CASCADE)
	source_title	= models.CharField(max_length=200, blank=True, null=True)
	topic			= MultiSelectField(max_length=100, choices=HC_TOPIC_CHOICES, null=True, blank=True)
	authors			= models.CharField(max_length=300, blank=True, null=True)
	upload_file_1	= models.FileField(upload_to="humancapital/posts/%Y/", max_length=100, blank=True, null=True, default="None")
	upload_file_2	= models.FileField(upload_to="humancapital/posts/%Y/", max_length=100, blank=True, null=True, default="None")
	upload_file_3	= models.FileField(upload_to="humancapital/posts/%Y/", max_length=100, blank=True, null=True, default="None")
	url_link_1		= models.URLField(max_length=100, blank=True, null=True)
	url_link_2		= models.URLField(max_length=100, blank=True, null=True)
	url_link_3		= models.URLField(max_length=100, blank=True, null=True)
	notes			= models.TextField(max_length=500, blank=True, null=True)
	timestamp_added	= models.DateTimeField(auto_now_add=True)
	timestamp_updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-timestamp_added']

	def __str__(self):
		return self.source_title

	def get_absolute_url(self):
		return reverse('humancapital:sources_listview')

	@property
	def relative_path(self):
		return os.path.relpath(self.path, settings.MEDIA_ROOT)

	@property
	def title(self):
		return self.title
