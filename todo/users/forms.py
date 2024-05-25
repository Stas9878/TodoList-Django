from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Повтор пароля')

    class Meta:
        model = get_user_model()
        fields = ['username','email','password1','password2'] 
        labels = {
            'username': 'Имя',
            'email': 'Электронный адрес',
        }
        help_texts = {
            'username': 'Ivan123',
            'email': 'ivan-123@todo.com',
        }
        


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100, 
        label='Имя пользователя или email',
        help_text='Ivan123 / ivan-123@todo.com')
        
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    
    class Meta:
        model = get_user_model()