from django import forms
from .models import PostComment

class PostCommentForm(forms.ModelForm):
    post = forms.CharField(empty_value = 3)
    class Meta:
        model = PostComment
        fields = ('fullname',  'email', 'comment', 'post')
        widgets = {'post': forms.HiddenInput()}
