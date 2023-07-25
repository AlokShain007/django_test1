# Generated by Django 4.2.2 on 2023-07-20 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_employee_details_owner_owner_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_details', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='myapp.owner'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intern_name', models.CharField(max_length=100)),
                ('intern_details', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interns', to='myapp.employee')),
            ],
        ),
        migrations.AddField(
            model_name='owner',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owners', to='myapp.company'),
            preserve_default=False,
        ),
    ]