from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author_name', 'description', 'address', 'blood_group', 'required_bags', 'deadline', 'contact_number']