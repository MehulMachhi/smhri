# Generated by Django 4.1.4 on 2022-12-20 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_companymaster_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymaster',
            name='test',
            field=models.CharField(blank=True, choices=[('AudiometerThresholdDecimats', 'AudiometerThresholdDecimats'), ('BloodTest', 'BloodTest'), ('Complaints', 'Complaints'), ('Hematology', 'Hematology'), ('LungFunctionTest', 'LungFunctionTest'), ('MicroscopicExamination', 'MicroscopicExamination'), ('OtherTests', 'OtherTests'), ('PhysiologicalTest', 'PhysiologicalTest'), ('SystematicExamination', 'SystematicExamination'), ('VisualTest', 'VisualTest')], max_length=222, null=True),
        ),
    ]
