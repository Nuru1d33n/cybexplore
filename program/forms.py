from django import forms
from program.models import UserProgram

# form-input

class UserProgramForm(forms.ModelForm):
    instagram_url = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    facebook_url = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    twitter_url = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    home_address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    occupation = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    state = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    # country = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control'
    #         }
    #     )
    # )
    # image = forms.CharField(
    #     widget=forms.FileInput(
    #         attrs={
    #             'class': 'form-control'
    #         }
    #     )
    # )
    # gender = forms.CharField(
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-control'
    #         }
    #     )
    # )

    # program = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control'
    #         }
    #     )
    # )
    name_of_school = forms.CharField(
        max_length= 255, 
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    

    class Meta:
        model = UserProgram
        fields = '__all__'
        exclude = ['school_name_required', 'course_price']
        widgets = {
            'course_price': forms.TextInput(attrs={'required': False}),
        }


