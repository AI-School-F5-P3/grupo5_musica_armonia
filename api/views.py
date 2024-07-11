from rest_framework import viewsets
from .models import Teacher, ClassPack, Instrument, Price, Classe, Level, TeacherClasse, Student, Enrollment, ClassPackDiscountRules, ClassPackClasse
from .serializers import TeacherSerializer, ClassPackSerializer, InstrumentSerializer, PriceSerializer, ClassesSerializer, LevelsSerializer, TeacherClassesSerializer, StudentsSerializer, EnrollmentsSerializer, ClassPackDiscountRulesSerializer, ClassPackClassesSerializer
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.apps import apps
from django.forms import modelform_factory



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
    serializer_class = ClassesSerializer

class LevelsViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelsSerializer

class TeacherClasseViewSet(viewsets.ModelViewSet):
    queryset = TeacherClasse.objects.all()
    serializer_class = TeacherClassesSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentsSerializer

class ClassPackDiscountRulesViewSet(viewsets.ModelViewSet):
    queryset = ClassPackDiscountRules.objects.all()
    serializer_class = ClassPackDiscountRulesSerializer

class ClassPackClasseViewSet(viewsets.ModelViewSet):
    queryset = ClassPackClasse.objects.all()
    serializer_class = ClassPackClassesSerializer


def index(request):
    return render(request, 'index.html')

def table_view(request, table):
    model = apps.get_model('api', table)
    data = model.objects.all()
    return render(request, 'table_view.html', {'data': data, 'table': table})

def create_entry(request, table):
    model = apps.get_model('api', table)
    FormClass = modelform_factory(model, exclude=[])
    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('table_view', args=[table]))
    else:
        form = FormClass()
    return render(request, 'create.html', {'form': form, 'table': table})

def update_entry(request, table, id):
    model = apps.get_model('api', table)
    instance = get_object_or_404(model, id=id)
    FormClass = modelform_factory(model, exclude=[])
    if request.method == 'POST':
        form = FormClass(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('table_view', args=[table]))
    else:
        form = FormClass(instance=instance)
    return render(request, 'update.html', {'form': form, 'table': table})

def delete_entry(request, table, id):
    model = apps.get_model('api', table)
    instance = get_object_or_404(model, id=id)
    if request.method == 'POST':
        instance.delete()
        return redirect(reverse('table_view', args=[table]))
    return render(request, 'delete_confirm.html', {'table': table, 'instance': instance})