# Generated by Django 4.2.2 on 2023-07-20 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_owner_remove_employee_interns_delete_intern'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='Employee_details',
            new_name='owner_details',
        ),
    ]
