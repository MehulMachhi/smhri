# Generated by Django 4.1.4 on 2022-12-21 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_master', '0007_alter_bloodtest_alkaline_phosphatase_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='allergic_to',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='family_health_history',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='id_mark_mole',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='id_mark_scar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='occupational_complaints',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='past_history',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='personal_health_history',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='present_complaints',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]