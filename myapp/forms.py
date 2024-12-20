from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
from django.contrib.auth import get_user_model
from .models import Class
from django.conf import settings
from .models import Quiz

class RegisterForm(UserCreationForm):
    # Add the 'role' field to the form
    role = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
        }),
        label='Select your role'
    )

    class Meta:
        model = CustomUser  # Use the CustomUser model instead of the default User model
        fields = ['username', 'email', 'password1', 'password2', 'role']  # Include 'role' in the fields
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your email'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Confirm your password'
            }),
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']  # Customize with any fields you want to edit
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your email'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your last name'
            }),
        }

User = get_user_model()

class ClassForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(
        queryset=User.objects.filter(role='teacher'),  # Tiyakin na may `role` field ang iyong user model
        label='Teacher'
    )

    class Meta:
        model = Class
        fields = ['name', 'teacher', 'max_students']


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['class_assigned', 'title', 'total_questions', 'max_attempts']