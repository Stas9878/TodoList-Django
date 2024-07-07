from django import forms
from django.contrib.auth import get_user_model

class UpdateUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False

    class Meta:
        model = get_user_model()
        fields = [
            'username', 'first_name', 
            'last_name', 'email', 
            'password'
        ]
        labels = {
            'password': 'Новый пароль'
        }
        
        