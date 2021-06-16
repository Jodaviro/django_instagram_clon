"""Users Form"""
# django
from django.forms import ModelForm
from posts.models import Post, Comment
from django.forms.widgets import FileInput, Textarea

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
        fields = ['post', 'user', 'text', 'likes', 'profile']
        exclude= ['user', 'likes', 'profile', 'post']
        widgets={'text': Textarea(attrs={
            'class': 'form-control',
            'cols' : 1,
            'rows': 1,
            'placeholder': 'Insert your comment',
            'required': True,
            'labels': False,
        }),
        }