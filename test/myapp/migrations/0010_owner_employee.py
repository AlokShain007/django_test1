# Generated by Django 4.2.2 on 2023-07-20 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_intern_employees_delete_company_delete_intern'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='Employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.employee'),
            preserve_default=False,
        ),
    ]