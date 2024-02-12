from django.shortcuts import render, redirect
from .models import EmployeeMaster
from django.http import HttpResponseRedirect
# from report.models import EmployeeReports
from report.models import SummaryReport
from company.models import CompanyMaster
from .decoder import convert_to_base64
from test_master.models import *
from datetime import datetime
from django.http import HttpResponseBadRequest
# Create your views here.
from datetime import datetime
from django.shortcuts import redirect
from django.urls import reverse

###################### ADD Employee Code ####################

def add_employees_data(request):
    if request.method == "POST":
        list_company = request.POST.get('list_company')
        name_pref = request.POST.get('name_pref')
        test_type = request.POST.get('test_type')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        sex = request.POST.get('sex')
        company = request.POST.get('company')
        employee_no = request.POST.get('employee_no')
        ticket_no = request.POST.get('ticket_no')
        aadhar_card_no = request.POST.get('aadhar_card_no')
        pan_number = request.POST.get('pan_number')
        
        if request.POST.get('date_joining'):
            date_joining = request.POST.get('date_joining')
        else:
            date_joining = None
        
        
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        address = request.POST.get('address')
        # country = request.POST.get('country')
        # state = request.POST.get('state')
        city = request.POST.get('city')
        
        
        if request.POST.get('birthdate'):
            birthdate = request.POST.get('birthdate')
        else:
            birthdate = None
        # try:
        #     birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()  # convert the string to a date object
        # except ValueError:
        # handle the case where the date string is invalid
        # return HttpResponseBadRequest('Invalid date format')
        photo = request.POST.get('photo')
        if photo:
            string = convert_to_base64(photo)
        else:
            string = None
        
        if request.POST.get('fitness_certificate_date'):
            fitness_certificate_date = request.POST.get('fitness_certificate_date')
        else:
            fitness_certificate_date = None
        
        previous_certificate_number = request.POST.get('previous_certificate_number')
        
        collection_date = request.POST.get('collection_date')
        # collection_date = datetime.strptime(collection_date_str, '%Y-%m-%d').date()
        
        test_date = request.POST.get('test_date')
        # test_date = datetime.strptime(test_date_str, '%Y-%m-%d').date()
        
        
        # collection_date = request.POST.get('collection_date')
        # collection_date_str = request.POST.get("collection_date")
        # collection_date = datetime.strptime(collection_date_str, '%Y-%m-%d').date()
        
        # test_date_str = request.POST.get('test_date')
        # test_date = datetime.strptime(test_date_str, '%Y-%m-%d').date()
        
        status = request.POST.get('status')
        show = "yes"
        # with open("photo.txt", "wb") as e:
        #     file = photo
        #     e.write(file)
        try:
            list_company = CompanyMaster.objects.get(id=list_company)
        except Exception as e:
            list_company = list_company
        # AudiometerThresholdDecimats = request.POST.get('AudiometerThresholdDecimats')
        # BloodTest = request.POST.get('BloodTest')
        # Complaints = request.POST.get('Complaints')
        # Hematology = request.POST.get('Hematology')
        # LungFunctionTest = request.POST.get('LungFunctionTest')
        # MicroscopicExamination = request.POST.get('MicroscopicExamination')
        # OtherTests = request.POST.get('OtherTests')
        # PhysiologicalTest = request.POST.get('PhysiologicalTest')
        # SystematicExamination = request.POST.get('SystematicExamination')
        # VisualTest = request.POST.get('VisualTest')
        if str('data')=='Yes':
            print('in if ')
        # data = EmployeeMaster(
        #     first_name=first_name
        # )
        data = EmployeeMaster(list_company=list_company, name_pref=name_pref,test_type=test_type, first_name=first_name, middle_name=middle_name, last_name=last_name, sex= sex, company=company, employee_no=employee_no, ticket_no=ticket_no, aadhar_card_no=aadhar_card_no, pan_number=pan_number,
            date_joining=date_joining, designation=designation, department=department, address=address,  city=city, birthdate=birthdate, photo=string, fitness_certificate_date=fitness_certificate_date,
            previous_certificate_number=previous_certificate_number, collection_date=collection_date,test_date=test_date, status=status, show=show)
        data.save()
        companydata = AudiometerThresholdDecimats(audio_employee= data)
        companydata.save()
        companydata = BloodTest(btest_employee= data)
        companydata.save()
        companydata = Urine_Examination(urine_employee= data)
        companydata.save()
        companydata = Complaints(complaints_employee= data)
        companydata.save()
        companydata = Hematology(hlogy_employee= data)
        companydata.save()
        companydata = LungFunctionTest(lung_employee= data)
        companydata.save()
        companydata = MicroscopicExamination(micro_employee= data)
        companydata.save()
        companydata = OtherTests(othertest_employee= data)
        companydata.save()
        companydata = PhysiologicalTest(phy_employee= data)
        companydata.save()
        companydata = SystematicExamination(sys_employee= data)
        companydata.save()
        companydata = VisualTest(visual_employee= data)
        companydata.save()
        new_data_id = data.id
        
        
        # SummaryReport.objects.create(employee_name=data)
        # data = EmployeeMaster(
        #     name_pref=name_pref, first_name=first_name, middle_name=middle_name, last_name=last_name, sex=sex, company=company, employee_no=employee_no, ticket_no=ticket_no, aadhar_card_no=aadhar_card_no, pan_number=pan_number,
        #     date_joining=date_joining, designation=designation, department=department, address=address, country=country, state=state, city=city, birthdate=birthdate, photo=photo, fitness_certificate_date=fitness_certificate_date,
        #     previous_certificate_number=previous_certificate_number, collection_date=collection_date,test_date=test_date,status=status,AudiometerThresholdDecimats=AudiometerThresholdDecimats,
        #     BloodTest=BloodTest, Complaints=Complaints, Hematology=Hematology, LungFunctionTest=LungFunctionTest, MicroscopicExamination=MicroscopicExamination, OtherTests=OtherTests, PhysiologicalTest=PhysiologicalTest,
        #     SystematicExamination=SystematicExamination, VisualTest=VisualTest)
        # data.save()
        # EmployeeReports.objects.create(first_name=data)
        # return render(request, 'view-employees-new.html')
        # return redirect('/crm/profile/?id=' + str(new_data_id))
        return redirect('/crm/add_employees_data')
        # return redirect(reverse('/crm/profile', args=[new_data_id]))
    else:
        context = {'companies' : CompanyMaster.objects.all().values('id','name')}
        print('-----------------------------------------dsd---',context)
        return render(request, 'view-employees-new.html',context)

# def add_employees_data(request):
#     if request.method == "POST":
#         post = EmployeeMaster()
#         post.first_name = request.POST.get('first_name')
#         # post.email = request.POST.get('email')
#         # post.phone = request.POST.get('phone')
#         # post.pincode = request.POST.get('pincode')
#         # post.company_registration_certificate = request.POST.get('company_registration_certificate')
#         # post.address = request.POST.get('address')
#         # post.country = request.POST.get('country')
#         # post.test = request.POST.get('test')
#         post.save()
#         alldata = EmployeeMaster.objects.all()
#         return render(request, 'view-companies.html', {"stu": alldata})
#     else:
#         return render(request, 'view-companies.html')

###################### View Employee Code ####################

# def view_employees_data(request):
#     return render(request, 'view-employees.html', {'s'})
from silk.profiling.profiler import silk_profile
@silk_profile(name='view_employees_data')

def view_employees_data(request):
    if request.method == "GET":
        alldata = EmployeeMaster.objects.filter(show="yes").order_by('-id').select_related(
            "list_company",
            )
       
        return render(request, 'view-employees.html', {"stu": alldata})
    return render(request, 'view-employees.html')

###################### Edit Employee Code ####################

# def edit_employees_data(request):
#     alldata = EmployeeMaster.objects.all()
#     return redirect(request, 'view-employees.html', {"stu": alldata})

###################### UPDATE Employee Code ####################

# def update_employees_data(request, id):
#     stu = EmployeeMaster.objects.get(id=id)
#     vuser = EmployeeMaster.objects.all()
#     if request.method == "POST":
#         app.name_pref = request.POST.get('name_pref')
#         app.first_name = request.POST.get('first_name')
#         app.middle_name = request.POST.get('middle_name')
#         app.last_name = request.POST.get('last_name')
#         app.sex = request.POST.get('sex')
#         app.company = request.POST.get('company')
#         app.ticket_no = request.POST.get('ticket_no')
#         app.aadhar_card_no = request.POST.get('aadhar_card_no')
#         app.pan_number = request.POST.get('pan_number')
#         app.date_joining = request.POST.get('date_joining')
#         app.designation = request.POST.get('designation')
#         app.department = request.POST.get('department')
#         app.address = request.POST.get('address')
#         app.country = request.POST.get('country')
#         app.state = request.POST.get('state')
#         app.city = request.POST.get('city')
#         app.birthdate = request.POST.get('birthdate')
#         app.photo = request.POST.get('photo')
#         app.fitness_certificate_date = request.POST.get('fitness_certificate_date')
#         app.previous_certificate_number = request.POST.get('previous_certificate_number')
#         app.test_type = request.POST.get('test_type')
#         app.collection_date = request.POST.get('collection_date')
#         app.test_date = request.POST.get('test_date')
#         app.status = request.POST.get('status')
#         app.audiometerThresholdDecimats = request.POST.get('audiometerThresholdDecimats')
#         app.bloodTest = request.POST.get('bloodTest')
#         app.complaints = request.POST.get('complaints')
#         app.hematology = request.POST.get('hematology')
#         app.lungFunctionTest = request.POST.get('lungFunctionTest')
#         app.microscopicExamination = request.POST.get('microscopicExamination')
#         app.otherTests = request.POST.get('otherTests')
#         app.physiologicalTest = request.POST.get('physiologicalTest')
#         app.systematicExamination = request.POST.get('systematicExamination')
#         app.visualTest = request.POST.get('visualTest')
#         app.save()
#         return render(request, 'view-employees.html', {"stu": app})
#     return render(request, 'view-employees.html')

###################### EDIT Employee Code ####################

# def edit_employees_data(request, id):
#     alldata = EmployeeMaster.objects.get(id=id)
#     return render(request, 'update-employees.html', {"stu": alldata})

###################### UPDATE Employee Code ####################

def update_employees_data(request, id):
    # uuser = EmployeeMaster.objects.get(id=id)
    # vuser = EmployeeMaster.objects.all()
    if EmployeeMaster.objects.filter(id=id):
        obj=EmployeeMaster.objects.get(id=id)
        
    uuser = EmployeeMaster.objects.get(id=id)
    vuser = EmployeeMaster.objects.all()
    if request.method == 'POST':
        list_company =  request.POST.get('list_company')
        name_pref = request.POST.get('name_pref')
        test_type = request.POST.get('test_type')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        sex = request.POST.get('sex')
        company = request.POST.get('company')
        employee_no = request.POST.get('employee_no')
        ticket_no = request.POST.get('ticket_no')
        aadhar_card_no = request.POST.get('aadhar_card_no')
        pan_number = request.POST.get('pan_number')
        date_joining = request.POST.get('date_joining')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        address = request.POST.get('address')
        # country = request.POST.get('country')
        # state = request.POST.get('state')
        city = request.POST.get('city')
        birthdate = request.POST.get('birthdate')
        photo = request.POST.get('photo')
        fitness_certificate_date = request.POST.get('fitness_certificate_date')
        previous_certificate_number = request.POST.get('previous_certificate_number')
        collection_date = request.POST.get('collection_date')
        test_date = request.POST.get('test_date')
        status = request.POST.get('status')
        
        try:
            list_company = CompanyMaster.objects.get(id=list_company)
        except Exception as e:
            list_company = list_company
            
        # audiometerThresholdDecimats = request.POST.get('audiometerThresholdDecimats')
        # bloodTest = request.POST.get('bloodTest')
        # complaints = request.POST.get('complaints')
        # hematology = request.POST.get('hematology')
        # lungFunctionTest = request.POST.get('lungFunctionTest')
        # microscopicExamination = request.POST.get('microscopicExamination')
        # otherTests = request.POST.get('otherTests')
        # physiologicalTest = request.POST.get('physiologicalTest')
        # systematicExamination = request.POST.get('systematicExamination')
        # visualTest = request.POST.get('visualTest')
        
        EmployeeMaster.objects.filter(pk=id).update(list_company=list_company, name_pref=name_pref, test_type=test_type, first_name=first_name, middle_name=middle_name, last_name=last_name, sex= sex, company=company, employee_no=employee_no, ticket_no=ticket_no, aadhar_card_no=aadhar_card_no, pan_number=pan_number,
            date_joining=date_joining, designation=designation, department=department, address=address, city=city, birthdate=birthdate, photo=photo, fitness_certificate_date=fitness_certificate_date,
            previous_certificate_number=previous_certificate_number, collection_date=collection_date, test_date=test_date,  status=status)
            
        # EmployeeMaster.objects.filter(pk=id).update(
        #     name_pref=name_pref, first_name=first_name, middle_name=middle_name, last_name=last_name, sex=sex, company=company, employee_no=employee_no, ticket_no=ticket_no, aadhar_card_no=aadhar_card_no, pan_number=pan_number,
        #     date_joining=date_joining, designation=designation, department=department, address=address, city=city, birthdate=birthdate, photo=photo, fitness_certificate_date=fitness_certificate_date,
        #     previous_certificate_number=previous_certificate_number, collection_date=collection_date,test_date=test_date,status=status,audiometerThresholdDecimats=audiometerThresholdDecimats,
        #     bloodTest=bloodTest, complaints=complaints, hematology=hematology, lungFunctionTest=lungFunctionTest, microscopicExamination=microscopicExamination, otherTests=otherTests, physiologicalTest=physiologicalTest,
        #     systematicExamination=systematicExamination, visualTest=visualTest)
        # return render(request, 'update-employees.html', {'vuser': vuser})
        return redirect('/crm/view_employees_data')
        
    # else:
    #     uuser = EmployeeMaster.objects.get(id=id)
    #     return render(request, 'update-employees.html', {'uuser': uuser})
    else:
        context = {'companies' : CompanyMaster.objects.all().values('id','name'), 'uuser':uuser}
        # print('-----------------------------------------dsd---',context)
        return render(request, 'update-employees.html',context)

def delete_employees_data(request, id):
    delete = EmployeeMaster.objects.get(id=id)
    EmployeeMaster.objects.filter(id=id).update(show="no")
    return redirect('/crm/view_employees_data')


def profile(request, id):
    # uuser = EmployeeMaster.objects.get(id=id)
    # vuser = EmployeeMaster.objects.all()
    # if EmployeeMaster.objects.filter(id=id):
    #     obj=EmployeeMaster.objects.get(id=id)
    uuser = EmployeeMaster.objects.get(id=id)
    # uCompANY  = CompanyMaster.objects.get(id=uuser.company)
    # vuser = EmployeeMaster.objects.all()
    if request.method == 'POST':
        list_company =  request.POST.get('list_company')
        name_pref = request.POST.get('name_pref')
        test_type = request.POST.get('test_type')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        sex = request.POST.get('sex')
        company = request.POST.get('company')
        employee_no = request.POST.get('employee_no')
        ticket_no = request.POST.get('ticket_no')
        aadhar_card_no = request.POST.get('aadhar_card_no')
        pan_number = request.POST.get('pan_number')
        date_joining = request.POST.get('date_joining')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        address = request.POST.get('address')
        city = request.POST.get('city')
        
        birthdate = request.POST.get('birthdate')
        if not birthdate:
            birthdate = None
            
        # photo = request.POST.get('photo')
        fitness_certificate_date = request.POST.get('fitness_certificate_date')
        previous_certificate_number = request.POST.get('previous_certificate_number')
        collection_date = request.POST.get('collection_date')
        test_date = request.POST.get('test_date')
        status = request.POST.get('status')
        
        photo = request.POST.get('photo')
        # if photo:
            
        uid = id
        # with open('logfile.txt', 'w') as e:
        #     e.write(photo)
        
        # with open('logfilestr.txt', 'w') as e:
        #     e.write(string)
        # if photo:
        # else:
        #     string = 0
        # try:
        #     list_company = CompanyMaster.objects.get(id=list_company)
        # except Exception as e:
        #     list_company = list_company
        if photo:
            string = convert_to_base64(photo)
            uuser.photo = string 
            uuser.save()
        EmployeeMaster.objects.filter(pk=id).update(list_company=list_company, name_pref=name_pref, test_type=test_type, first_name=first_name, middle_name=middle_name, last_name=last_name, sex= sex, company=company, employee_no=employee_no, ticket_no=ticket_no, aadhar_card_no=aadhar_card_no, pan_number=pan_number,
            date_joining=date_joining, designation=designation, department=department, address=address, city=city, birthdate=birthdate, fitness_certificate_date=fitness_certificate_date,
            previous_certificate_number=previous_certificate_number, collection_date=collection_date, test_date=test_date,  status=status)
            
        # EmployeeMaster.objects.filter(pk=id).update(
        #     name_pref=name_pref, first_name=first_name, middle_name=middle_name, last_name=last_name, sex=sex, company=company, employee_no=employee_no, ticket_no=ticket_no, aadhar_card_no=aadhar_card_no, pan_number=pan_number,
        #     date_joining=date_joining, designation=designation, department=department, address=address, city=city, birthdate=birthdate, photo=photo, fitness_certificate_date=fitness_certificate_date,
        #     previous_certificate_number=previous_certificate_number, collection_date=collection_date,test_date=test_date,status=status,audiometerThresholdDecimats=audiometerThresholdDecimats,
        #     bloodTest=bloodTest, complaints=complaints, hematology=hematology, lungFunctionTest=lungFunctionTest, microscopicExamination=microscopicExamination, otherTests=otherTests, physiologicalTest=physiologicalTest,
        #     systematicExamination=systematicExamination, visualTest=visualTest)
        # return render(request, 'update-employees.html', {'vuser': vuser})
        # return redirect('/crm/view_employees_data')
        return redirect(request.META['HTTP_REFERER'])
        
    # else:
    #     uuser = EmployeeMaster.objects.get(id=id)
    #     return render(request, 'update-employees.html', {'uuser': uuser})
    # else:
    #     context = {'companies' : CompanyMaster.objects.all().values('id','name'), 'uuser':uuser}
    #     # print('-----------------------------------------dsd---',context)
    #     return render(request, 'update-employees.html',context)
      
    else:
        context = {'companies' : CompanyMaster.objects.all().values('id','name'), 'profile_data':uuser, 'uid' : id,'company_id' : uuser.list_company_id, 'alltest':uuser.list_company.test}
        # print('-----------------------------------------dsd---',context)
        return render(request, 'profile.html',context)


def audiometery1(request):
    return render(request, 'AUDIOMETERY.html')
    
def biochemistry(request):
    return render(request, 'BIOCHEMISTRY.html')












