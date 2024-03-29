# Generated by Django 4.1.5 on 2023-02-01 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_master', '0029_alter_bloodtest_alkaline_phosphatase_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urine_examination',
            name='epi_cells',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='urine_examination',
            name='ph_reaction',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='urine_examination',
            name='pus_cells',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='urine_examination',
            name='rbc',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='urine_examination',
            name='sp_gravity',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
    ]
