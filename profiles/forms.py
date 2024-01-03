from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'image', 'group_name']
        
    def __init__(self, *args, **kwargs):
        super(ProfileForm,self).__init__(*args ,**kwargs)
            
            
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__(*args ,**kwargs)
            