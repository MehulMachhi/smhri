# Generated by Django 5.0.2 on 2024-02-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='companymaster',
            name='company_registration_certificate',
            field=models.ImageField(blank=True, max_length=222, null=True, upload_to='media'),
        ),
    ]
