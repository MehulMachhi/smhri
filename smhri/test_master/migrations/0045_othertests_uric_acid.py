# Generated by Django 4.1.5 on 2023-04-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_master', '0044_rename_employee_physiologicaltest_phy_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='othertests',
            name='uric_acid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
