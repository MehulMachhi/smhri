# Generated by Django 4.1.5 on 2023-04-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0043_alter_employeemaster_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemaster',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
