"""User Form models """
#django
from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['website', 'phone_number' , 'picture', 'biography']



