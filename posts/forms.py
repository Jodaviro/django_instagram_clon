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
        fields = ['user', 'profile', 'title', 'photo', 'likes']
        exclude=['user', 'profile','likes']
        widgets = {'photo': FileInput(attrs={'class': 'form-control'}),

         }


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['post', 'user', 'text', 'likes']
        exclude= ['post', 'user', 'likes']
        widgets={'text': Textarea(attrs={
            'class': 'form-control',
            'cols': 1,
            'rows': 2,
            'placeholder': 'Insert your comment',
            'required': True,
            'label': False,
        }),
        }