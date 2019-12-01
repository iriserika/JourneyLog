from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
	comment = forms.CharField(
		label = "Comment", 
		widget = forms.Textarea(
			attrs = {
			"placeholder": "Enter comment",
			"class": "form-control",
			"rows": 3,
		}))
	class Meta:
		model = Comment
		fields = ['comment']

