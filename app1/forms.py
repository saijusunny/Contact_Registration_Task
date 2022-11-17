from .models import Contact
from django import forms
from django.contrib.auth.models import User, Group


class ContactForm(forms.ModelForm):
    # user=forms.ModelChoiceField(queryset=Group.objects.all())
    class Meta:
        model = Contact
        fields = ['name','pic','mobile','email']

