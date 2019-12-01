from django import forms

from .models import Note

class PostForm(forms.ModelForm):
	title = forms.CharField(
		label = "Note Title", 
		widget = forms.Textarea(
			attrs = {
			"placeholder": "Enter title",
			"class": "form-control",
			"rows": 3,
		}))
	text = forms.CharField(
		label = "Note Text", 
		widget = forms.Textarea(
			attrs = {
			"placeholder": "Enter text",
			"class": "form-control",
			"rows": 10,
		}))
	cover = forms.ImageField(
		label = "Cover Image"
		)
	tagChoices = [
		('Weekend', 'Weekend Break'),
		('Short', 'Short Term'),
		('Long', 'Long Term'),
		('Gap', 'Gap Year'),
		]
	tag = forms.CharField(
		label = "Duration",
		widget = forms.RadioSelect(
			choices=tagChoices,
		))
	class Meta:
		model = Note
		fields = ['title', 'text', 'cover', 'tag']
