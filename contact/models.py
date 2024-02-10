from django.db import models

# Create your models here.
class Contact(models.Model):
    '''Model definition for Contact.'''
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()
    # date_sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''Meta definition for Contact.'''

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    