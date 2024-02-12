from django.db import models

# Create your models here.

class AudiometerThresholdDecimats(models.Model):
        # audio_th_dec_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        audio_employee = models.ForeignKey("employee.EmployeeMaster", on_delete=models.CASCADE, null=True, blank=True)
        right_ac_500 = models.CharField(max_length=222,  null=True, blank=True)
        right_bc_500 = models.CharField(max_length=222, null=True, blank=True)
        right_ac_1000 = models.CharField(max_length=222,  null=True, blank=True)
        right_bc_1000 = models.CharField(max_length=222, null=True, blank=True)
        right_ac_2000 = models.CharField(max_length=222, null=True, blank=True)
        right_bc_2000 = models.CharField(max_length=222, null=True, blank=True)
        right_ac_4000 = models.CharField(max_length=222, null=True, blank=True)
        right_bc_4000 = models.CharField(max_length=222, null=True, blank=True)
        right_ac_5000 = models.CharField(max_length=222, null=True, blank=True)
        right_bc_5000 = models.CharField(max_length=222, null=True, blank=True)
        left_ac_500 = models.CharField(max_length=222, null=True, blank=True)
        left_bc_500 = models.CharField(max_length=222, null=True, blank=True)
        left_ac_1000 = models.CharField(max_length=222, null=True, blank=True)
        left_bc_1000 = models.CharField(max_length=222, null=True, blank=True)
        left_ac_2000 = models.CharField(max_length=222, null=True, blank=True)
        left_bc_2000 = models.CharField(max_length=222, null=True, blank=True)
        left_ac_4000 = models.CharField(max_length=222, null=True, blank=True)
        left_bc_4000 = models.CharField(max_length=222, null=True, blank=True)
        left_ac_5000 = models.CharField(max_length=222, null=True, blank=True)
        left_bc_5000 = models.CharField(max_length=222, null=True, blank=True)
        for_right_ear = models.CharField(max_length=222, null=True, blank=True)
        for_left_ear = models.CharField(max_length=222, null=True, blank=True)
        audiometery = models.CharField(max_length=222, null=True, blank=True)
        xray_report = models.CharField(max_length=222, null=True, blank=True)
        ultra_sonographic = models.CharField(max_length=222, null=True, blank=True)
        
        def __str__(self):
             return str(self.right_ac_500)
           
        
class BloodType(models.TextChoices):
    O_positive = "O-positive", "O-positive"
    O_negative = "O-negative", "O-negative"
    A_positive = "A-positive", "A-positive"
    A_negative = "A-negative", "A-negative"
    B_positive = "B-positive", "B-positive"
    B_negative = "B-negative", "B-negative"
    AB_positive = "AB-positive", "AB-positive"
    AB_negative = "AB-negative", "AB-negative"

class BloodTest(models.Model):
        # blood_test_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        btest_employee = models.ForeignKey("employee.EmployeeMaster", on_delete=models.CASCADE, null=True, blank=True)
        blood_group = models.CharField(max_length=200, null=True, blank=True, choices=BloodType.choices)
        blood_cholestrol = models.CharField(max_length=222, null=True, blank=True)
        creatinine = models.CharField(max_length=222,null=True, blank=True)
        blood_urea = models.CharField(max_length=222,null=True, blank=True)
        fasting_blood_glucose = models.CharField(max_length=222,null=True, blank=True)
        random_blood_glucose = models.CharField(max_length=222, null=True, blank=True)
        post_prandial_blood_glucose = models.CharField(max_length=222, null=True, blank=True)
        total_bilirubin = models.CharField(max_length=222, null=True, blank=True)
        direct_bilirubin = models.CharField(max_length=222, null=True, blank=True)
        indirect_bilirubin = models.CharField(max_length=222, null=True, blank=True)
        sgpt = models.CharField(max_length=222, null=True, blank=True)
        sgot = models.CharField(max_length=222, null=True, blank=True)
        alkaline_phosphatase = models.CharField(max_length=222, null=True, blank=True)
        ggt = models.CharField(max_length=222, null=True, blank=True)
        total_cholesterol = models.CharField(max_length=222, null=True, blank=True)
        triglycerides = models.CharField(max_length=222, null=True, blank=True)
        direct_hdl = models.CharField(max_length=222, null=True, blank=True)
        vldl = models.CharField(max_length=222, null=True, blank=True)
        ldl = models.CharField(max_length=222, null=True, blank=True)
        ch_ratio = models.CharField(max_length=222, null=True, blank=True)
        lh_ratio = models.CharField(max_length=222, null=True, blank=True)
        rdw_sd = models.CharField(max_length=222, null=True, blank=True)  # Field name made lowercase.
        plcc = models.CharField(max_length=222, null=True, blank=True)  # Field name made lowercase.
        plcr = models.CharField(max_length=222, null=True, blank=True)  # Field name made lowercase.
        vitaminb12 = models.CharField(max_length=222, null=True, blank=True)
        vitamind3 = models.CharField(max_length=222, null=True, blank=True)
        hcv = models.CharField(max_length=222, null=True, blank=True)
        psa = models.CharField(max_length=222, null=True, blank=True)
        bun = models.CharField(max_length=222, null=True, blank=True)
        
        def __str__(self):
             return str(self.blood_cholestrol)
           
        
        

class  Urine_Examination(models.Model):
        urine_employee = models.ForeignKey("employee.EmployeeMaster", on_delete=models.CASCADE,  null=True, blank=True)
        volume = models.CharField(max_length=222,  null=True, blank=True)
        transparency = models.CharField(max_length=255,  null=True, blank=True)
        deposit = models.CharField(max_length=255,  null=True, blank=True)
        colour = models.CharField(max_length=255,  null=True, blank=True)
        sp_gravity = models.CharField(max_length=255, null=True, blank=True)
        ph_reaction = models.CharField(max_length=255, null=True, blank=True)
        pus_cells = models.CharField(max_length=255, null=True, blank=True)
        rbc = models.CharField(max_length=255, null=True, blank=True)
        epi_cells = models.CharField(max_length=255, null=True, blank=True)
        casts = models.CharField(max_length=225,  null=True, blank=True)
        crystals = models.CharField(max_length=255,  null=True, blank=True)
        bacteria = models.CharField(max_length=255,  null=True, blank=True)
        yeast_cells = models.CharField(max_length=255,  null=True, blank=True)
        trichomonas = models.CharField(max_length=255,  null=True, blank=True)
        amorphous_deposit = models.CharField(max_length=255,  null=True, blank=True)
        albumin = models.CharField(max_length=255,  null=True, blank=True)
        sugar = models.CharField(max_length=255,  null=True, blank=True)
        acetone = models.CharField(max_length=255,  null=True, blank=True)
        bile_pigments = models.CharField(max_length=255,  null=True, blank=True)
        bile_salts = models.CharField(max_length=255,  null=True, blank=True)
        urobilinogen = models.CharField(max_length=255,  null=True, blank=True)

        red_blood_cells = models.CharField(max_length=50, null=True, blank=True)
        epithelial_cells = models.CharField(max_length=50, null=True, blank=True)
        urine_report = models.CharField(max_length=50, null=True, blank=True)
        crystais = models.CharField(max_length=50, null=True, blank=True)
        material = models.CharField(max_length=255,  null=True, blank=True)
        

        def __str__(self):
             return str(self.volume)
             
# class family_health_type(models.TextChoices):
#     hypertension = "hypertension", "hypertension"
#     diabetes = "diabetes", "diabetes"
class family_class_type(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

class Complaints(models.Model):
        # complaint_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        # blood_group = models.CharField(max_length=200, null=True, blank=True, choices=BloodType.choices)
        complaints_employee = models.ForeignKey("employee.EmployeeMaster", on_delete=models.CASCADE,  null=True, blank=True)
        present_complaints = models.CharField(max_length=255, null=True, blank=True)
        occupational_complaints = models.CharField(max_length=255, null=True, blank=True)
        family_health_history = models.ManyToManyField(family_class_type,null=True, blank=True,)
        personal_health_history = models.CharField(max_length=255, null=True, blank=True)
        past_history = models.CharField(max_length=255, null=True, blank=True)
        allergic_to = models.CharField(max_length=255, null=True, blank=True)
        id_mark_scar = models.CharField(max_length=255, null=True, blank=True)
        id_mark_mole = models.CharField(max_length=255, null=True, blank=True)
        

        def __str__(self):
             return str(self.occupational_complaints)




class Hematology(models.Model):
        # hematology_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        hlogy_employee = models.ForeignKey("employee.EmployeeMaster", on_delete=models.CASCADE,  null=True, blank=True)
        blood_group = models.CharField(max_length=50,  null=True, blank=True)
        hemoglobin = models.CharField(max_length=50,  null=True, blank=True)
        total_wbc_count = models.CharField(max_length=50, null=True, blank=True)
        polymorphs = models.CharField(max_length=50, null=True, blank=True)
        lymphocytes = models.CharField(max_length=50, null=True, blank=True)
        eosinophils = models.CharField(max_length=50, null=True, blank=True)
        monocytes = models.CharField(max_length=50, null=True, blank=True)
        basophils = models.CharField(max_length=50, null=True, blank=True)
        leucocytes_count = models.CharField(max_length=50, null=True, blank=True)
        platelet_count = models.CharField(max_length=50, null=True, blank=True)
        esr = models.CharField(max_length=50, null=True, blank=True)
        hct = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.
        rdw_cv = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.
        pdw = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.
        mpv = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.
        mch = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.
        mchc = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.
        pct = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.
        mcv = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.
        peripheral_smear = models.CharField(max_length=50, null=True, blank=True)
        
        
        def __str__(self):
             return str(self.polymorphs)





class LungFunctionTest(models.Model):
        # lung_function_test_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        lung_employee = models.ForeignKey("employee.EmployeeMaster", on_delete=models.CASCADE,  null=True, blank=True)
        fvc = models.CharField(max_length=50, null=True, blank=True)
        fev1 = models.CharField(max_length=50, null=True, blank=True)
        fev1_fvc = models.CharField(max_length=50, null=True, blank=True)
        peak_exp_flow = models.CharField(max_length=50, null=True, blank=True)
        fef50 = models.CharField(max_length=50, null=True, blank=True)
        fvc_predicted = models.CharField(max_length=50, null=True, blank=True)
        fev1_predicted = models.CharField(max_length=50, null=True, blank=True)
        fev1_fvc_predicted = models.CharField(max_length=50, null=True, blank=True)
        pefr_predicted = models.CharField(max_length=50, null=True, blank=True)
        fef50_predicted = models.CharField(max_length=50, null=True, blank=True)
        fvc_per_predicted = models.CharField(max_length=50, null=True, blank=True)
        fev1_per_predicted = models.CharField(max_length=50, null=True, blank=True)
        fev1_fvc_per_predicted = models.CharField(max_length=50, null=True, blank=True)
        pefr_per_predicted = models.CharField(max_length=50, null=True, blank=True)
        fef50_per_predicted = models.CharField(max_length=50, null=True, blank=True)
        spirometry = models.CharField(max_length=50, null=True, blank=True)
        
        def __str__(self):
             return str(self.fev1)




class MicroscopicExamination(models.Model):
        # micro_exam_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        micro_employee = models.ForeignKey("employee.EmployeeMaster", on_delete=models.CASCADE,  null=True, blank=True)
        red_blood_cells = models.CharField(max_length=50, null=True, blank=True)
        pus_cells = models.CharField(max_length=50, null=True, blank=True)
        epithelial_cells = models.CharField(max_length=50, null=True, blank=True)
        urine_report = models.CharField(max_length=50, null=True, blank=True)
        casts = models.CharField(max_length=50, null=True, blank=True)
        crystais = models.CharField(max_length=50, null=True, blank=True)
        material = models.CharField(max_length=255,  null=True, blank=True)
        
    
        def __str__(self):
             return str(self.pus_cells)



class OtherTests(models.Model):
        # othertest_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        othertest_employee = models.ForeignKey("employee.EmployeeMaster", on_delete=models.CASCADE, null=True, blank=True)
        uric_acid = models.CharField(max_length=255, null=True, blank=True)
        serum_cholinesterase = models.CharField(max_length=255, null=True, blank=True)
        hs_crp = models.CharField(max_length=255, null=True, blank=True)
        gppd = models.CharField(max_length=255, null=True, blank=True)
        hba1c = models.CharField(max_length=255, null=True, blank=True)
        avg_blood_glucose_level = models.CharField(max_length=255, null=True, blank=True)
        hbsag = models.CharField(max_length=255, null=True, blank=True)
        hiv_result = models.CharField(max_length=255, null=True, blank=True)
        hiv_method = models.CharField(max_length=255, null=True, blank=True)
        hiv_remark = models.CharField(max_length=255, null=True, blank=True)
        s_protein_total = models.CharField(max_length=255, null=True, blank=True)
        s_albumin_bcg = models.CharField(max_length=255, null=True, blank=True)
        s_globulin = models.CharField(max_length=255, null=True, blank=True)
        ag_ratio = models.CharField(max_length=255, null=True, blank=True)
        acid_fast_bacilli = models.CharField(max_length=200, null=True, blank=True)
        stool_color = models.CharField(max_length=255, null=True, blank=True)
        stool_blood = models.CharField(max_length=255, null=True, blank=True)
        stool_mucus = models.CharField(max_length=255, null=True, blank=True)
        stool_adults_warm = models.CharField(max_length=255, null=True, blank=True)
        stool_parasites = models.CharField(max_length=255,null=True, blank=True)
        stool_pus = models.CharField(max_length=255, null=True, blank=True)
        stool_ph = models.CharField(max_length=255, null=True, blank=True)
        stool_occult_blood = models.CharField(max_length=255, null=True, blank=True)
        stool_reducing_substances = models.CharField(max_length=255,null=True, blank=True)
        stool_rbcs = models.CharField(max_length=255, null=True, blank=True)
        stool_puscells = models.CharField(max_length=255, null=True, blank=True)
        stool_fat_globules = models.CharField(max_length=255, null=True, blank=True)
        stool_macrophages = models.CharField(max_length=255, null=True, blank=True)
        stool_epithelial_cell = models.CharField(max_length=255, null=True, blank=True)
        stool_muscle_fibers = models.CharField(max_length=255, null=True, blank=True)
        stool_vegetable_cell = models.CharField(max_length=255, null=True, blank=True)
        stool_bacteria = models.CharField(max_length=255, null=True, blank=True)
        stool_cyst = models.CharField(max_length=255, null=True, blank=True)
        stool_ova = models.CharField(max_length=255, null=True, blank=True)
        stool_trophozoites = models.CharField(max_length=255, null=True, blank=True)
        stool_larva = models.CharField(max_length=255, null=True, blank=True)
        stool_yeast_cells = models.CharField(max_length=255, null=True, blank=True)
        stool_starch_granules = models.CharField(max_length=255,null=True, blank=True)
        thyroid_tsh = models.CharField(max_length=255, null=True, blank=True)
        thyroid_t3 = models.CharField(max_length=255, null=True, blank=True)
        thyroid_t4 = models.CharField(max_length=255, null=True, blank=True)
        vdrl = models.CharField(max_length=255, null=True, blank=True)
        
    
        def __str__(self):
             return str(self.serum_cholinesterase)




class PhysiologicalTest(models.Model):
        # phy_test_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        phy_employee = models.ForeignKey("employee.EmployeeMaster", on_delete=models.CASCADE,  null=True, blank=True)
        height = models.CharField(max_length=255, null=True, blank=True)
        weight = models.CharField(max_length=255, null=True, blank=True)
        blood_pressure = models.CharField(max_length=255, null=True, blank=True)
        pulse = models.CharField(max_length=255, null=True, blank=True)
        heart_sound = models.CharField(max_length=255, null=True, blank=True)
        chest_on_expiration = models.CharField(max_length=255, null=True, blank=True)
        chest_on_inspiration = models.CharField(max_length=255, null=True, blank=True)
        waist = models.CharField(max_length=255, null=True, blank=True)
        hips = models.CharField(max_length=255, null=True, blank=True)
        waist_hip_ratio = models.CharField(max_length=255, null=True, blank=True)
        remarks_and_advice = models.CharField(max_length=255, null=True, blank=True)
        
        
        def __str__(self):
            return str(self.height)



class SystematicExamination(models.Model):
        # sys_exm_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        sys_employee = models.ForeignKey("employee.EmployeeMaster", on_delete=models.CASCADE,  null=True, blank=True)
        skin = models.CharField(max_length=100,  null=True, blank=True)
        respiratory_system = models.CharField(max_length=255,  null=True, blank=True)
        cardiovascular_system = models.CharField(max_length=255,  null=True, blank=True)
        genito_urinary_system = models.CharField(max_length=255,  null=True, blank=True)
        skeletal_system = models.CharField(max_length=255,  null=True, blank=True)
        cns = models.CharField(max_length=255,  null=True, blank=True)
        breath_sound = models.CharField(max_length=255,  null=True, blank=True)
        abdomen = models.CharField(max_length=255,  null=True, blank=True)
        other_finding = models.CharField(max_length=255,  null=True, blank=True)
        ecg_report = models.CharField(max_length=255,  null=True, blank=True)

        def __str__(self):
            return str(self.skin)




class VisualTest(models.Model):
        # visual_test_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        visual_employee = models.ForeignKey("employee.EmployeeMaster", on_delete=models.CASCADE,  null=True, blank=True)
        nearvision_without_glass = models.CharField(max_length=255, null=True, blank=True)
        distance_vision_without_glass = models.CharField(max_length=255, null=True, blank=True)
        nearvision_with_glass = models.CharField(max_length=255, null=True, blank=True)
        distance_vision_with_glass = models.CharField(max_length=255, null=True, blank=True)
        nearvision_without_glass_right = models.CharField(max_length=255, null=True, blank=True)
        distance_vision_without_glass_right = models.CharField(max_length=255, null=True, blank=True)
        nearvision_with_glass_right = models.CharField(max_length=255, null=True, blank=True)
        distance_vision_with_glass_right = models.CharField(max_length=255, null=True, blank=True)
        vision_remark = models.CharField(max_length=255, null=True, blank=True)
        
   
        def __str__(self):
            return str(self.nearvision_without_glass)




class TestMaster(models.Model):
        # test_id = models.AutoField(primary_key=True)
        test_name = models.CharField(max_length=255,  null=True, blank=True)
        test_desc = models.CharField(max_length=255,  null=True, blank=True)
        status = models.CharField(max_length=255,  null=True, blank=True)
        test_model = models.CharField(max_length=255,  null=True, blank=True)

        def __str__(self):
            return str(self.test_name)


















