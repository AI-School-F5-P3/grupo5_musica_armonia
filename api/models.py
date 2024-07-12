from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'teacher'

class ClassPack(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'classpack'

class Instrument(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'instrument'

class Price(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        db_table = 'prices'

class Classe(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'classe'

class Level(models.Model):
    name = models.CharField(max_length=100)
    _class = models.ForeignKey(Classe, on_delete=models.CASCADE, db_column='_class_id')

    class Meta:
        db_table = 'level'

class TeacherClasse(models.Model):
    _class = models.ForeignKey(Classe, on_delete=models.CASCADE, db_column='_class_id')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, db_column='teacher_id')

    class Meta:
        db_table = 'teacherclasse'

class ClassPackDiscountRules(models.Model):
    class_pack = models.ForeignKey(ClassPack, on_delete=models.CASCADE)
    class_number = models.IntegerField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        db_table = 'classpackdiscountrule'

class ClassPackClasse(models.Model):
    _class = models.ForeignKey(Classe, on_delete=models.CASCADE, db_column='_class_id')
    class_pack = models.ForeignKey(ClassPack, on_delete=models.CASCADE, db_column='class_pack_id')

    class Meta:
        db_table = 'classpackclasse' 

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15, default=1)
    email = models.EmailField(default='default@example.com')  # Proveer un valor por defecto
    family_discount = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'student'

class Enrollment(models.Model):
    enrollment_date = models.DateField()
    class_number = models.IntegerField()
    _class = models.ForeignKey(Classe, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, default=1)  # Proveer un valor por defecto
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=1)  # Proveer un valor por defecto
    
    class Meta:
        db_table = 'enrollment'
