from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CertificateForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    student = forms.ModelChoiceField(queryset=Student.objects.all())

    class Meta:
        model = Certificate
        fields = ['teacher','student']

class StudentForm(forms.ModelForm):
    teachers = forms.ModelMultipleChoiceField(
        queryset=Teacher.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Student
        fields = ["name",'email']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'email']