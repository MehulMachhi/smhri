# Generated by Django 4.1.4 on 2022-12-21 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_master', '0003_rename_xray_reports_audiometerthresholddecimats_xray_report'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bloodtest',
            old_name='s_creatinine',
            new_name='creatinine',
        ),
    ]