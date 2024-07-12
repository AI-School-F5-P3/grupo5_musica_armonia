from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Teacher, ClassPack, Instrument, Price, Classe, Level, TeacherClasse, Student, Enrollment, ClassPackDiscountRules, ClassPackClasse
from .serializers import TeacherSerializer, ClassPackSerializer, InstrumentSerializer, PriceSerializer, ClasseSerializer, LevelSerializer, TeacherClasseSerializer, StudentSerializer, EnrollmentSerializer, ClassPackDiscountRulesSerializer, ClassPackClasseSerializer
from .forms import EnrollmentForm, StudentForm

# API ViewSets
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ClassPackViewSet(viewsets.ModelViewSet):
    queryset = ClassPack.objects.all()
    serializer_class = ClassPackSerializer

class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

class LevelsViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class TeacherClasseViewSet(viewsets.ModelViewSet):
    queryset = TeacherClasse.objects.all()
    serializer_class = TeacherClasseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class ClassPackDiscountRulesViewSet(viewsets.ModelViewSet):
    queryset = ClassPackDiscountRules.objects.all()
    serializer_class = ClassPackDiscountRulesSerializer

class ClassPackClasseViewSet(viewsets.ModelViewSet):
    queryset = ClassPackClasse.objects.all()
    serializer_class = ClassPackClasseSerializer

# Function-Based Views
def index(request):
    return render(request, 'index.html')

def show_tables(request):
    students = Student.objects.all()
    enrollments = Enrollment.objects.all()
    return render(request, 'show_tables.html', {'students': students, 'enrollments': enrollments})

def new_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tables')
    else:
        form = EnrollmentForm()
    return render(request, 'new_enrollment.html', {'form': form})

def new_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tables')
    else:
        form = StudentForm()
    return render(request, 'new_student.html', {'form': form})

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('show_tables')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('show_tables')
    return render(request, 'delete_student.html', {'student': student})

def update_enrollment(request, id):
    enrollment = get_object_or_404(Enrollment, id=id)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('show_tables')
    else:
        form = EnrollmentForm(instance=enrollment)
    return render(request, 'update_enrollment.html', {'form': form})

def delete_enrollment(request, id):
    enrollment = get_object_or_404(Enrollment, id=id)
    if request.method == 'POST':
        enrollment.delete()
        return redirect('show_tables')
    return render(request, 'delete_enrollment.html', {'enrollment': enrollment})
