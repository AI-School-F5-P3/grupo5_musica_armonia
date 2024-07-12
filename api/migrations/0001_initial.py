# Generated by Django 5.0.6 on 2024-07-12 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'classes',
            },
        ),
        migrations.CreateModel(
            name='ClassPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'classpacks',
            },
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'instruments',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'prices',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(default=1, max_length=15)),
                ('email', models.EmailField(default='default@example.com', max_length=254)),
                ('family_discount', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
        migrations.CreateModel(
            name='ClassPackClasse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_class', models.ForeignKey(db_column='_class_id', on_delete=django.db.models.deletion.CASCADE, to='api.classe')),
                ('class_pack', models.ForeignKey(db_column='class_pack_id', on_delete=django.db.models.deletion.CASCADE, to='api.classpack')),
            ],
            options={
                'db_table': 'classpackclasses',
            },
        ),
        migrations.CreateModel(
            name='ClassPackDiscountRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_number', models.IntegerField()),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('class_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classpack')),
            ],
            options={
                'db_table': 'classpackdiscountrules',
            },
        ),
        migrations.AddField(
            model_name='classe',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.instrument'),
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('_class', models.ForeignKey(db_column='_class_id', on_delete=django.db.models.deletion.CASCADE, to='api.classe')),
            ],
            options={
                'db_table': 'levels',
            },
        ),
        migrations.AddField(
            model_name='classe',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.price'),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField()),
                ('class_number', models.IntegerField()),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classe')),
                ('level', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.level')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
                ('teacher', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.teacher')),
            ],
            options={
                'db_table': 'enrollments',
            },
        ),
        migrations.CreateModel(
            name='TeacherClasse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_class', models.ForeignKey(db_column='_class_id', on_delete=django.db.models.deletion.CASCADE, to='api.classe')),
                ('teacher', models.ForeignKey(db_column='teacher_id', on_delete=django.db.models.deletion.CASCADE, to='api.teacher')),
            ],
            options={
                'db_table': 'teacherclasses',
            },
        ),
    ]
