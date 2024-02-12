# Generated by Django 4.1.4 on 2023-01-11 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0025_remove_employeemaster_list_company'),
        ('report', '0003_summaryreport_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employeemaster')),
            ],
        ),
    ]
