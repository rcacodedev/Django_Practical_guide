from django import forms
from .models import Review
# class ReviewForm(forms.Form):
    # username = forms.CharField(label="Your name", max_length=100, error_messages={'required': 'Please enter your name',
                                                                                    # 'max_length': 'Your name is too long'})
    # review_text = forms.CharField(label="Your feedback", widget=forms.Textarea, max_length=200)
    # rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["username", "review_text", "rating"] # Also if you want use all field from the database you can use '__all__'
        labels = {
            "username": "Your name",
            "review_text": "Your feedback",
            "rating": "Your rating",
        }
        error_messages = {
            "username": {
                "required": "Please enter your name",
                "max_length": "Your name is too long",
            },
            "rating": {
                "min_value": "Please enter a value between 1 and 5",
                "max_value": "Please enter a value between 1 and 5",
            },
        }