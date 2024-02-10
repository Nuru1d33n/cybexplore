from django import forms
from review.models import Rating

class RateForm(forms.Form):
    class Meta:
        model = Rating
        # fields = ('user','profile','heading','content',)
        fields = '_all__'
        # exclude = ('user','profile',)
