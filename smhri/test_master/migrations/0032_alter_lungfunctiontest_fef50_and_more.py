# Generated by Django 4.1.5 on 2023-02-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_master', '0031_alter_hematology_basophils_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fef50',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fef50_per_predicted',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fef50_predicted',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fev1',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fev1_fvc',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fev1_fvc_per_predicted',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fev1_fvc_predicted',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fev1_per_predicted',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fev1_predicted',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fvc',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fvc_per_predicted',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='fvc_predicted',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='peak_exp_flow',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='pefr_per_predicted',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='pefr_predicted',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lungfunctiontest',
            name='spirometry',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='microscopicexamination',
            name='casts',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='microscopicexamination',
            name='crystais',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='microscopicexamination',
            name='epithelial_cells',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='microscopicexamination',
            name='pus_cells',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='microscopicexamination',
            name='red_blood_cells',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='microscopicexamination',
            name='urine_report',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='ag_ratio',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='avg_blood_glucose_level',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='gppd',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='hba1c',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='hbsag',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='hiv_method',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='hiv_remark',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='hiv_result',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='hs_crp',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='s_albumin_bcg',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='s_globulin',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='s_protein_total',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='serum_cholinesterase',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_adults_warm',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_bacteria',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_blood',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_color',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_cyst',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_epithelial_cell',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_fat_globules',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_larva',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_macrophages',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_mucus',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_muscle_fibers',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_occult_blood',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_ova',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_parasites',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_ph',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_pus',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_puscells',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_rbcs',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_reducing_substances',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_starch_granules',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_trophozoites',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_vegetable_cell',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_yeast_cells',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='thyroid_t3',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='thyroid_t4',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='thyroid_tsh',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='vdrl',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
    ]
