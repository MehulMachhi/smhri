# Generated by Django 4.1.4 on 2023-01-12 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0025_remove_employeemaster_list_company'),
        ('test_master', '0010_alter_urine_examination_pus_cells'),
    ]

    operations = [
        migrations.AddField(
            model_name='physiologicaltest',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.employeemaster'),
            preserve_default=False,
        ),
    ]
