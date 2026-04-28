from django import forms
from django.contrib.auth.models import User
from .models import Property

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['confirm_password']:
            raise forms.ValidationError("Passwords do not match")


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ["property_owner"]

from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            "title",
            "location",
            "rent",
            "bedrooms",
            "bathrooms",
            "parking",
            "balcony",
            "wifi",
            "washing_machine",
            "description",
        ]

    



     