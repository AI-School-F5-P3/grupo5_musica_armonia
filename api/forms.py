from django import forms
from .models import Student, Teacher, Classe, Enrollment, Price, ClassPack

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class ClassForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = '__all__'

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'

class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = '__all__'

class ClassPackForm(forms.ModelForm):
    class Meta:
        model = ClassPack
        fields = '__all__'