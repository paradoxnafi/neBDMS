from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'address', 'blood_group', 'required_bags', 'deadlineDate', 'deadlineTime', 'contact_number']