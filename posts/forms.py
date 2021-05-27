"""Users Form"""
# django
from django.forms import ModelForm
from posts.models import Post, Comment
from django.forms.widgets import FileInput, Select, NumberInput, Textarea

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


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['post', 'user', 'text', 'likes']
        exclude= ['post', 'user', 'likes']
        widgets={'text': Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Insert your comment',
            'required': True,
        }),
        }