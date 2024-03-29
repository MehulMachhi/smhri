# Generated by Django 4.1.5 on 2023-02-01 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_master', '0037_alter_microscopicexamination_casts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fef50',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fef50_per_predicted',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fef50_predicted',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fev1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fev1_fvc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fev1_fvc_per_predicted',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fev1_fvc_predicted',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fev1_per_predicted',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fev1_predicted',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fvc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fvc_per_predicted',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fvc_predicted',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='peak_exp_flow',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='pefr_per_predicted',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='pefr_predicted',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='spirometry',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
