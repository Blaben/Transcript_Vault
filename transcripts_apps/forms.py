from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Student, Course, Grade


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "index_number", "program", "level"]


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["course_code", "course_title", "credit_hours"]


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["student", "course", "grade", "semester", "level", "academic_year"]