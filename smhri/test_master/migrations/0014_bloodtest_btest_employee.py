# Generated by Django 4.1.4 on 2023-01-12 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0026_employeemaster_list_company'),
        ('test_master', '0013_systematicexamination_sys_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodtest',
            name='btest_employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.employeemaster'),
            preserve_default=False,
        ),
    ]
