from django import forms
from .models import PostComment

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('fullname',  'email', 'comment',)