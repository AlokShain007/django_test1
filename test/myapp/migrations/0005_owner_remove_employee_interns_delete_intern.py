# Generated by Django 4.2.2 on 2023-07-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_employee_interns'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=100)),
                ('Employee_details', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='interns',
        ),
        migrations.DeleteModel(
            name='Intern',
        ),
    ]
