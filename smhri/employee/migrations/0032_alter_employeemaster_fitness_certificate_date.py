# Generated by Django 4.1.5 on 2023-02-28 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0031_alter_employeemaster_collection_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemaster',
            name='fitness_certificate_date',
            field=models.CharField(blank=True, default='2021-01-01', max_length=155, null=True),
        ),
    ]
