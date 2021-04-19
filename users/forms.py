"""User Form models """
#django
from django.forms.widgets import FileInput, NumberInput
from django.forms import ModelForm
from .models import Profile
from posts.models import Post

class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['website', 'phone_number' , 'picture', 'biography']
        widgets = {'picture': FileInput(attrs={'class' : 'form-control'}),
            'pone_number': NumberInput(attrs={
            'class': 'form-control',
            'type': 'number',
            }),

        }

