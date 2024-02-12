# Generated by Django 4.1.5 on 2023-02-01 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_master', '0025_alter_othertests_acid_fast_bacilli'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='audiometery',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='for_left_ear',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='for_right_ear',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='left_ac_1000',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='left_ac_2000',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='left_ac_4000',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='left_ac_500',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='left_ac_5000',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='left_bc_1000',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='left_bc_2000',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='left_bc_4000',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='left_bc_500',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='left_bc_5000',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='right_ac_1000',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='right_ac_2000',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='right_ac_4000',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='right_ac_500',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='right_ac_5000',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='right_bc_1000',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='right_bc_2000',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='right_bc_4000',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='right_bc_500',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='right_bc_5000',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='ultra_sonographic',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='audiometerthresholddecimats',
            name='xray_report',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
    ]
