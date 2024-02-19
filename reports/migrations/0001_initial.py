# Generated by Django 5.0.2 on 2024-02-19 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0002_remove_companymaster_company_registration_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('date', models.DateField()),
                ('message', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChemicalExamination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField()),
                ('transparency', models.IntegerField()),
                ('deposit', models.IntegerField()),
                ('colour', models.CharField(max_length=50)),
                ('sp_gravity', models.IntegerField()),
                ('ph_reaction', models.IntegerField()),
                ('pus_cells', models.IntegerField()),
                ('rbc', models.IntegerField()),
                ('epi_cells', models.IntegerField()),
                ('casts', models.CharField(max_length=50)),
                ('crystals', models.IntegerField()),
                ('bacteria', models.CharField(max_length=50)),
                ('yeast_cells', models.IntegerField()),
                ('trichomonas', models.IntegerField()),
                ('amorphous_deposit', models.IntegerField()),
                ('albumin', models.IntegerField()),
                ('sugar', models.IntegerField()),
                ('acetone', models.IntegerField()),
                ('bile_pigments', models.IntegerField()),
                ('bile_salts', models.IntegerField()),
                ('urobilinogen', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=250)),
                ('state', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DiffierentialCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neutrophils', models.CharField(max_length=25)),
                ('eosinophil', models.CharField(max_length=25)),
                ('monocytes', models.CharField(max_length=25)),
                ('basophil', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('message', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=250)),
                ('country', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('company', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=30)),
                ('photo', models.ImageField(max_length=255, upload_to='')),
                ('role', models.CharField(max_length=10)),
                ('password', models.TextField()),
                ('last_login', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('banned_users', models.CharField(max_length=100)),
                ('user_com', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SummaryReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=200)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companymaster')),
            ],
        ),
    ]
