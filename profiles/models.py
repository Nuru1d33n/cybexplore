from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

User = get_user_model()

class UserProfile(models.Model):
	first_name = models.CharField(max_length=264, blank=True)
	last_name = models.CharField(max_length=264, blank=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
	image = models.ImageField(upload_to='static/profile_pics', blank=True, default="static/assets/img/avatar.jpg")
	description = models.TextField(blank=True)
	dob = models.DateField(blank=True, null=True)
	facebook_url = models.URLField(blank=True)
	twitter_url = models.URLField(blank=True)
	instagram_url = models.URLField(blank=True)

	# @receiver(post_save, sender=User)
	# def create_user_profile(sender, instance, created, **kwargs):
	# 	if created:
	# 		UserProfile.objects.create(user=instance)

	# @receiver(post_save, sender=User)
	# def save_user_profile(sender, instance, **kwargs):
	# 	instance.profile.save()



	def __str__(self):
		return self.user.email + " profile"




