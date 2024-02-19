# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from company.models import CompanyMaster

# from employee.models import EmployeeMaster

class Appoinment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date = models.DateField()
    message = models.CharField(max_length=255)

class ChemicalExamination(models.Model):
    # chem_exam = models.AutoField(primary_key=True)
    # emp_id = models.IntegerField()
    volume = models.IntegerField()
    transparency = models.IntegerField()
    deposit = models.IntegerField()
    colour = models.CharField(max_length=50)
    sp_gravity = models.IntegerField()
    ph_reaction = models.IntegerField()
    pus_cells = models.IntegerField()
    rbc = models.IntegerField()
    epi_cells = models.IntegerField()
    casts = models.CharField(max_length=50)
    crystals = models.IntegerField()
    bacteria = models.CharField(max_length=50)
    yeast_cells = models.IntegerField()
    trichomonas = models.IntegerField()
    amorphous_deposit = models.IntegerField()
    albumin = models.IntegerField()
    sugar = models.IntegerField()
    acetone = models.IntegerField()
    bile_pigments = models.IntegerField()
    bile_salts = models.IntegerField()
    urobilinogen = models.IntegerField()

class City(models.Model):
    # city = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=250)
    state = models.IntegerField()

class Country(models.Model):
    # country = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=250)

class DiffierentialCount(models.Model):
    # diff_count = models.AutoField(primary_key=True)
    # emp_id = models.IntegerField()
    neutrophils = models.CharField(max_length=25)
    eosinophil = models.CharField(max_length=25)
    monocytes = models.CharField(max_length=25)
    basophil = models.CharField(max_length=25)

class Enquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.IntegerField()
    message = models.CharField(max_length=255)

# class Newsletter(models.Model):
#     email = models.CharField(max_length=255)

# class Settings(models.Model):
#     site_title = models.CharField(max_length=50)
#     timezone = models.CharField(max_length=100)
#     recaptcha = models.CharField(max_length=5)
#     theme = models.CharField(max_length=100)

class State(models.Model):
    # state = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=250)
    country = models.IntegerField()

# class Tokens(models.Model):
#     token = models.CharField(max_length=255)
#     user = models.IntegerField()
#     created = models.DateField()

class UserCompany(models.Model):
    # user_company = models.AutoField(primary_key=True)
    user = models.IntegerField()
    company = models.IntegerField()

class Users(models.Model):
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    photo = models.ImageField(max_length=255)
    role = models.CharField(max_length=10)
    password = models.TextField()
    last_login = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    banned_users = models.CharField(max_length=100)
    user_com = models.IntegerField(blank=True, null=True)


class SummaryReport(models.Model):
    company_name = models.ForeignKey(CompanyMaster, on_delete=models.CASCADE)
    action = models.CharField(max_length=200)


# class EmployeeReports(models.Model):
#     first_name = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE)
    # employee_no_emp = models.ManyToManyField(EmployeeMaster)
    # ticket_no_emp = models.ManyToManyField(EmployeeMaster)
    # department_emp = models.ManyToManyField(EmployeeMaster)
    # status_emp = models.ManyToManyField(EmployeeMaster)