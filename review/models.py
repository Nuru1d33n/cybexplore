from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from profiles.models import UserProfile

# Create your models here.

User = get_user_model()

# class Review(models.Model):
#     user_profile = models.ForeignKey(User, on_delete=models.CASCADE)

class RatingChoices(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    __empty__ = 'Unknown'

class Rating(models.Model):
    '''Model definition for Review.'''
    user = models.ForeignKey(User, related_name='user',  on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, related_name='profile', on_delete=models.CASCADE)
    heading = models.CharField(max_length=200)
    content = models.TextField()
    # rate = models.IntegerField()
    rate = models.IntegerField(null=True, blank=True, choices=RatingChoices.choices)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        '''Meta definition for Review.'''

        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

    def __str__(self):
        return "Review from " + self.user.email
    
    