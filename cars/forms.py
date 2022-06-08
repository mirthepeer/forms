from dataclasses import fields
from .models import Review
from django import forms

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name,', max_length=30)
#     last_name = forms.CharField(label = 'Last Nane', max_length=30)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please wirte your review here',widget=forms.Textarea())

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

    