from django.db import models
from django_countries.fields import CountryField
from course.models import Course

# Create your models here.

class UserProgram(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    COURSE_CHOICES = [
        ('CEH', 'Cybersecurity & Ethical Hacking'),
        ('WAPT', 'Web Application Penetration Testing'),
        ('FST', 'Full-Stack Web Development'),
        ('FD', 'Frontend Development'),
        ('BD', 'Backend Development'),
        ('HT', 'Hacking Tools'),
    ]
    

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='static/user_images/', blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    facebook_url = models.URLField(max_length=200)
    twitter_url = models.URLField(max_length=200)
    instagram_url = models.URLField(max_length=200)
    home_address = models.CharField(max_length=150)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=200,  null=True, choices=CountryField().choices + [('', 'Select Country')])
    program = models.ForeignKey(Course, on_delete=models.CASCADE)
    are_you_a_student = models.BooleanField()
    school_name_required = models.BooleanField(default=False)
    name_of_school = models.CharField(max_length=255, blank=True, null=True)
    do_you_have_laptop = models.BooleanField()
    occupation = models.CharField(max_length=50)
    # course_price = models.IntegerField(null=True, blank=True)
    

    def save(self, *args, **kwargs):
        # course_price_mapping = {
        #     'CEH': 35000,
        #     'WAPT': 30000,
        #     'FST': 35000,
        #     'FD': 15000,
        #     'BD': 15000,
        #     'HT': 40000,
        # }
        # if self.program in course_price_mapping:
        #     self.course_price = course_price_mapping[self.program]
        
        if self.are_you_a_student:
            self.school_name_required = True
        else:
            self.school_name_required = True
            self.name_of_school = None
            
        super().save(*args, **kwargs)
        
    # class Meta:
    #     abstract = True
        

    def __str__(self):
        return f"{self.email} ====> {self.program}"


