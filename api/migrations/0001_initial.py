# Generated by Django 5.0.6 on 2024-07-08 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='ClassPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Class_Packs',
            },
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Instruments',
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
                'db_table': 'Prices',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('family_discount', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Teachers',
            },
        ),
        migrations.CreateModel(
            name='ClassPackClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classes')),
                ('class_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classpack')),
            ],
            options={
                'db_table': 'Class_Pack_Classes',
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
                'db_table': 'Class_Pack_Discount_Rules',
            },
        ),
        migrations.AddField(
            model_name='classes',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.instrument'),
        ),
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classes')),
            ],
            options={
                'db_table': 'Levels',
            },
        ),
        migrations.AddField(
            model_name='classes',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.price'),
        ),
        migrations.CreateModel(
            name='Enrollments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField()),
                ('class_number', models.IntegerField(default=1)),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classes')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.levels')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.students')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.teacher')),
            ],
            options={
                'db_table': 'Enrollments',
            },
        ),
        migrations.CreateModel(
            name='TeacherClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classes')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.teacher')),
            ],
            options={
                'db_table': 'Teacher_Classes',
            },
        ),
    ]
