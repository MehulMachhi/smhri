from django.db import models
from test_master.models import (AudiometerThresholdDecimats, BloodTest, Complaints, Hematology
, LungFunctionTest, MicroscopicExamination, OtherTests, PhysiologicalTest, SystematicExamination, VisualTest,
                                TestMaster)

from company.models import CompanyMaster

# Create your models here.

class EmployeeMaster(models.Model):
    list_company = models.ForeignKey(CompanyMaster, on_delete=models.CASCADE, blank=True, null=True)

    class name_pref(models.TextChoices):
        Mr = 'Mr.', ('Mr.')
        Mrs = 'Mrs.', ('Mrs.')
    name_pref = models.CharField(max_length=200, choices=name_pref.choices, blank=True, null=True)
    class test_type(models.TextChoices):
        Pre = 'Pre', ('Pre')
        Periodical = 'Periodical', ('Periodical')
    test_type = models.CharField(max_length=200, choices=test_type.choices, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    class sex(models.TextChoices):
        Male = 'Male', ('Male')
        Female = 'Female', ('Female')
        Others = 'Others', ('Others')
# , default='2021-01-01'
    sex = models.CharField(max_length=6, choices=sex.choices, blank=True, null=True)
    class company(models.TextChoices):
        Flat_Management_Company = 'Flat Management Company', ('Flat Management Company')
        Private_Limited_Company = 'Private Limited Company', ('Private Limited Company')
        Unlimited_Company = 'Unlimited Company', ('Unlimited Company')
        Limited_Liability_Partnership = 'Limited Liability Partnership', ('Limited Liability Partnership')
        Proprietary = 'Proprietary', ('Proprietary')
        Right_to_Management_Company = 'Right to Management Company', ('Right to Management Company')
        Community_Interest_Company = 'Community Interest Company', ('Community Interest Company')
        Public_Limited_Company = 'Public_Limited_Company', ('Public Limited Company')
    company = models.CharField(max_length=30, choices=company.choices, blank=True, null=True)
    # company = models.ForeignKey(CompanyMaster, on_delete=models.CASCADE)
    employee_no = models.CharField(max_length=100, blank=True, null=True)
    ticket_no = models.CharField(max_length=100, blank=True, null=True)
    aadhar_card_no = models.CharField(max_length=100, blank=True, null=True)
    # name_prif = models.CharField(max_length=4, blank=True, null=True)
    pan_number = models.CharField(max_length=200, blank=True, null=True)
    date_joining = models.CharField(max_length=200,blank=True, null=True, default='2021-01-01')
    designation = models.CharField(max_length=200, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    # father_name = models.CharField(max_length=100, blank=True, null=True)
    # mother_name = models.CharField(max_length=100, blank=True, null=True)
    # class country(models.TextChoices):
    #     country1 = 'country1', ('country1')
    #     country2 = 'country2', ('country2')
    #     country3 = 'country3', ('country3')
    #     country4 = 'country4', ('country4')
    #     country5 = 'country5', ('country5')
    # country = models.CharField(max_length=10, choices=country.choices, blank=True, null=True)
    # class state(models.TextChoices):
    #     state1 = 'state1', ('state1')
    #     state2 = 'state2', ('state2')
    #     state3 = 'state3', ('state3')
    #     state4 = 'state4', ('state4')
    #     state5 = 'state5', ('state5')
    # state = models.CharField(max_length=6, choices=state.choices, blank=True, null=True)
    class city(models.TextChoices):
        Vadodara = 'Vadodara', ('Vadodara')
        Ahemedabad = 'Ahemedabad', ('Ahemedabad')
        Bharuch = 'Bharuch', ('Bharuch')
        Rajkot = 'Rajkot', ('Rajkot')
        Surat = 'Surat', ('Surat')
        Anand = 'Anand', ('Anand')
    city = models.CharField(max_length=15, choices=city.choices, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='media', blank=True, null=True)
    # , default='2021-01-01'
    fitness_certificate_date = models.CharField(max_length=155, blank=True, null=True, default='2021-01-01')
    previous_certificate_number = models.CharField(max_length=255, blank=True, null=True)
    # test_type = models.CharField(max_length=10, blank=True, null=True)
    collection_date = models.DateField(blank=True, null=True)
    test_date = models.DateField(blank=True, null=True)
    class status(models.TextChoices):
        Approved = 'approved', ('approved')
        Pending = 'pending', ('pending')
    status = models.CharField(max_length=8, choices=status.choices, blank=True, null=True)
    # emp_added_date = models.DateTimeField()
    AudiometerThresholdDecimats = models.ForeignKey(AudiometerThresholdDecimats, on_delete=models.CASCADE, blank=True,null=True)
    BloodTest = models.ForeignKey(BloodTest, on_delete=models.CASCADE, blank=True, null=True)
    Complaints = models.ForeignKey(Complaints, on_delete=models.CASCADE, blank=True, null=True)
    Hematology = models.ForeignKey(Hematology, on_delete=models.CASCADE, blank=True, null=True)
    LungFunctionTest = models.ForeignKey(LungFunctionTest, on_delete=models.CASCADE, blank=True, null=True)
    MicroscopicExamination = models.ForeignKey(MicroscopicExamination, on_delete=models.CASCADE, blank=True, null=True)
    OtherTests = models.ForeignKey(OtherTests, on_delete=models.CASCADE, blank=True, null=True)
    PhysiologicalTest = models.ForeignKey(PhysiologicalTest,  on_delete=models.CASCADE, blank=True, null=True)
    SystematicExamination = models.ForeignKey(SystematicExamination,  on_delete=models.CASCADE, blank=True, null=True)
    VisualTest = models.ForeignKey(VisualTest,  on_delete=models.CASCADE, blank=True, null=True)
    class show(models.TextChoices):
        yes = 'yes', ('yes')
        no = 'no', ('no')
    show = models.CharField(max_length=8, choices=show.choices, blank=True, null=True)


    def __str__(self):
             return str(self.first_name)


# class AudiometerThresholdDecimats(models.Model):
#     # audio_th_dec_id = models.AutoField(primary_key=True)
#     # emp_id = models.IntegerField()
#     right_ac_500 = models.IntegerField()
#     right_bc_500 = models.IntegerField()
#     right_ac_1000 = models.IntegerField()
#     right_bc_1000 = models.IntegerField()
#     right_ac_2000 = models.IntegerField()
#     right_bc_2000 = models.IntegerField()
#     right_ac_4000 = models.IntegerField()-
#     right_bc_4000 = models.IntegerField()
#     right_ac_6000 = models.IntegerField()
#     right_bc_6000 = models.IntegerField()
#     left_ac_500 = models.IntegerField()
#     left_bc_500 = models.IntegerField()
#     left_ac_1000 = models.IntegerField()
#     left_bc_1000 = models.IntegerField()
#     left_ac_2000 = models.IntegerField()
#     left_bc_2000 = models.IntegerField()
#     left_ac_4000 = models.IntegerField()
#     left_bc_4000 = models.IntegerField()
#     left_ac_6000 = models.IntegerField()
#     left_bc_6000 = models.IntegerField()
#     for_right_ear = models.IntegerField()
#     for_left_ear = models.IntegerField()
#     audiometery = models.IntegerField()
#     xray_report = models.IntegerField()
#     ultra_sonographic = models.IntegerField()




# import datetime 
# class migration(models.Model):
#     time mode = mode.coding_field(max_length = 200)
#     chair  = mode

































