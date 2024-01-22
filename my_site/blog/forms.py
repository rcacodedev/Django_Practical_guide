from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            'user_name': 'Your Name',
            'text': 'Your Comment',
            'user_email': 'Your Email'
        }