# Generated by Django 4.1.5 on 2023-02-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_master', '0030_alter_urine_examination_epi_cells_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hematology',
            name='basophils',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='eosinophils',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='esr',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='hct',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='leucocytes_count',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='lymphocytes',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='mch',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='mchc',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='mcv',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='monocytes',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='mpv',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='pct',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='pdw',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='peripheral_smear',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='platelet_count',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='polymorphs',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='rdw_cv',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hematology',
            name='total_wbc_count',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
    ]