# Generated by Django 4.2.2 on 2023-07-22 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_company_intern_owner_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Owner',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='intern',
            old_name='Employee',
            new_name='employee',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='Company',
        ),
        migrations.AddField(
            model_name='owner',
            name='company',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.company'),
            preserve_default=False,
        ),
    ]