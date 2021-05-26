"""User Form models """
#django
from django.forms.widgets import FileInput, NumberInput, Textarea, TextInput, PasswordInput, EmailInput
from django import forms
from .models import Profile
from posts.models import Post
from django.core.exceptions import ValidationError

#models
from django.contrib.auth.models import User
from users.models import Profile, Contact

#Profile
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['picture', 'biography', 'website', 'phone_number','user']
        exclude =['user']
        widgets = {'picture': FileInput(attrs={'class' : 'form-control'}),
            'phone_number': NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '(optional)',
            'type': 'number',
            }),
            'website': TextInput(attrs={
            'class': 'form-control',
            'placeholder': '(optional)'
            }),
            'biography': Textarea(attrs={
            'cols':4,
            'rows': 4,
            'class': 'form-control',
            'placeholder': 'You must provide a small biography, or a profile picture.'
            }),
        }


    def clean(self):
        cleaned_data = super().clean()
        picture = cleaned_data.get('picture')
        biography = cleaned_data.get('biography')


        if not picture and not biography:
            raise ValidationError('You must provide a profile picture or a biography text to proceeed.')




#Signup
class SignUpForm (forms.Form):

    username = forms.CharField(max_length=50, min_length=4,label=False ,widget=TextInput(attrs={
        'class' : 'form-control mt-1',
        'placeholder': 'Username'
    }) )
    password = forms.CharField(label=False, min_length=6, widget=PasswordInput(attrs={
        'class' : 'form-control mt-1',
        'placeholder': 'Password'
    }) )
    password_confirm = forms.CharField(label=False, min_length=6, widget=PasswordInput(attrs={
        'class' : 'form-control mt-1',
        'placeholder': 'Confirm Password',

    }) )
    email = forms.CharField(label=False, max_length=100, required=False, widget=EmailInput(attrs={
        'class' : 'form-control mt-1',
        'placeholder': 'Email (optional)'
    }) )
    first_name = forms.CharField( label=False, required=False, max_length=50, min_length=4, widget=TextInput(attrs={
        'class' : 'form-control mt-1',
        'placeholder': 'First Name (optional)'
    }) )


    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data['username']
        #Chek if username already exist in the database
        check_duplicate = User.objects.filter(username=username)
        if not check_duplicate:
            return username
        else:
            raise ValidationError('Username already registered')

    def clean_email(self):
        email = self.cleaned_data['email']
        # Defaul value for empty email field is '', so we need to filter default value
        if email !='' :
            # Check if email already exist in the database
            check_duplicate = User.objects.filter(email=email)
            if not check_duplicate:
                return email
            else:
                raise ValidationError('Email already registered')
        else:
            return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm:

            if password != password_confirm :
                raise ValidationError("Passwords fields didn't match ")

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirm')

        user = User.objects.create_user(**data)
        #Also creates a Profile
        profile = Profile(user=user)
        profile.save()

        # And also creates contact system
        contact = Contact(profile=profile)
        contact.save()





