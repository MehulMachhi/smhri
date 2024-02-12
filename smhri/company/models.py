from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class CompanyMaster(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.CharField(max_length=200, blank=True, null=True) 
    company_registration_certificate = models.ImageField(upload_to='media', max_length=222, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    class country(models.TextChoices):
        India = 'India', ('India')
        Australia = 'Australia', ('Australia')
        Uk = 'Uk', ('Uk')
    country = models.CharField(choices=country.choices, max_length=222, null=True, blank=True,)
    class test(models.TextChoices):
        AudiometerThresholdDecimats = 'AudiometerThresholdDecimats', ('AudiometerThresholdDecimats')
        BloodTest = 'BloodTest', ('BloodTest')
        Complaints = 'Complaints', ('Complaints')
        Hematology = 'Hematology', ('Hematology')
        LungFunctionTest = 'LungFunctionTest', ('LungFunctionTest')
        MicroscopicExamination = 'MicroscopicExamination', ('MicroscopicExamination')
        OtherTests = 'OtherTests', ('OtherTests')
        PhysiologicalTest = 'PhysiologicalTest', ('PhysiologicalTest')
        SystematicExamination = 'SystematicExamination', ('SystematicExamination')
        VisualTest = 'VisualTest', ('VisualTest')
        Urine_Examination = 'Urine_Examination', ('Urine_Examination')
    test = models.CharField( max_length=222, null=True, blank=True)

    def __str__(self):
        return self.name


from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)











