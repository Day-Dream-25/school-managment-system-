from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.http import request

from sms_app.models import User, School, Teacher, Student
from django import forms


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'password', 'phone_no', 'address', 'roll'
        )


class SchoolForm(ModelForm):

    class Meta:
        model = School
        fields = (
            'user', 'name', 'city'
        )


class TeacherForm(ModelForm):

    class Meta:
        model = Teacher
        fields = ('user',
            'school',
            'birthdate', 'subject'
        )


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class LoginForm(AuthenticationForm):

    class Meta:

        model = User
        fields = ('username', 'password')

