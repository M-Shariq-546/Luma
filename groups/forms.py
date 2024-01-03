from django.forms import forms
from .models import Members


class memberInviteForm(forms.Form):
    class Meta:
        model = Members
        fields = [
            'email'
        ]