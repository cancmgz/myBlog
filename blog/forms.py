from django import forms
from .models import PostComment,Post

class PostCommentForm(forms.ModelForm):

    class Meta:
        model = PostComment
        fields = ('fullname',  'email', 'comment')