# Generated by Django 4.1.5 on 2023-03-10 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_alter_companymaster_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymaster',
            name='test',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
    ]