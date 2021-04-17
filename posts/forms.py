#dajango
from django.forms import ModelForm
from posts.models import Post

#form
class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['user', 'profile', 'title','photo']

