from django import forms
from profiles.models import UserProfile
from django.contrib.auth.models import User


class EditProfile(forms.ModelForm):
    dob = forms.DateField(
	    	widget=forms.TextInput(
	    			attrs={'type':'date',}
	    		)
	    	)

    class Meta:
        model = UserProfile
        fields = '__all__'
        # exclude = ('first_name', 'last_name','user',)
        exclude = ['user']

