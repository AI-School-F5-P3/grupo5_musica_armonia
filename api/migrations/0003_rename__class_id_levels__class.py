# Generated by Django 5.0.6 on 2024-07-09 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename__class_levels__class_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='levels',
            old_name='_class_id',
            new_name='_class',
        ),
    ]
