# Generated by Django 4.1.5 on 2023-03-31 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0041_employeemaster_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemaster',
            name='photo',
            field=models.ImageField(default=1, upload_to='media'),
            preserve_default=False,
        ),
    ]
