"""Users Form"""
# django
from django.forms import ModelForm
from posts.models import Post
from django.forms.widgets import FileInput, Select, NumberInput

# forms


class PostForm(ModelForm):
    """Post form"""

    class Meta:
        model = Post
        fields = ['user', 'profile', 'title', 'photo',]
        exclude=['user', 'profile']
        widgets = {'photo': FileInput(attrs={'class': 'form-control'}),
            'user': NumberInput(attrs={
                'type': 'hidden',
                'required': False,
                'class': 'form-control',
                # 'disabled': True,
            }),
            'profile': NumberInput(attrs={
                'type': 'hidden',
                'required': False,
                'class': 'form-control',
                # 'disabled': True,
            }),
         }

