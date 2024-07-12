from rest_framework import serializers
from .models import Teacher, ClassPack, Instrument, Price, Classe, Level, TeacherClasse, Student, Enrollment, ClassPackDiscountRules, ClassPackClasse

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class ClassPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPack
        fields = '__all__'

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class TeacherClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherClasse
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class ClassPackDiscountRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPackDiscountRules
        fields = '__all__'

class ClassPackClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPackClasse
        fields = '__all__'
