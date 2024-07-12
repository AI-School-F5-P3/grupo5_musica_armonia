from django import forms
from .models import Enrollment, Student

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['enrollment_date', 'class_number', '_class', 'level', 'student', 'teacher']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'phone', 'email', 'family_discount']
