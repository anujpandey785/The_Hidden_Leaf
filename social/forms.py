from django import forms
from social import models

class PostForm(forms.ModelForm):
    class Meta:
        model=models.Post
        fields = ['content','image']

    def save(self,commit=True):
        return super().save(commit=commit)


class PostCommentForm(forms.ModelForm):
    class Meta:
        model=models.Comment
        fields = ['content']

