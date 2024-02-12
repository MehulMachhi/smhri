from django.shortcuts import render, redirect
from .models import Appoinment, ChemicalExamination, City, Country, DiffierentialCount, Enquiry , State, UserCompany, Users
from .models import SummaryReport
from employee.models import EmployeeMaster
# from test_master.models import Hematology
from test_master.models import *
from test_master.models import BloodTest, PhysiologicalTest, OtherTests, Hematology, Urine_Examination, AudiometerThresholdDecimats, SystematicExamination, LungFunctionTest, VisualTest, Complaints
from datetime import date, datetime
import math
from company.models import CompanyMaster
# from test_master.models import OtherTests
from django.http import Http404


########################### Appoinment ################################

###################### ADD Report Code ####################

def add_report_appointment(request):
    if request.method == "POST":
        post = Appoinment()
        post.name = request.POST.get('name')
        post.email = request.POST.get('email')
        post.date = request.POST.get('date')
        post.message = request.POST.get('message')
        post.save()
        return render(request, 'add-report-appointment.html')
    else:
        return render(request, 'add-report-appointment.html')

###################### View Report Code ####################

def view_report_appointment(request):
    alldata = Appoinment.objects.all()
    return render(request, 'view-report-appointment.html', {'stu', alldata})

###################### Update Report Code ####################

def update_report_appointment(request):
    update = Appoinment.objects.get(id=id)
    update.save()
    return render(request, 'update-report-appointment.html', {"edit": update})

###################### Delete Report Code ####################

def delete_report_appointment(request):
    delete = Appoinment.objects.get(id=id)
    delete.delete()
    return redirect('/')

########################### Chemicalexamination ################################

###################### ADD Report Code ####################

def add_report_chemicalexamination(request):
    if request.method == "POST":
        post = ChemicalExamination()
        post.chem_exam = request.POST.get('chem_exam')
        post.emp_id = request.POST.get('emp_id')
        post.volume = request.POST.get('volume')
        post.transparency = request.POST.get('transparency')
        post.deposit = request.POST.get('deposit')
        post.colour = request.POST.get('colour')
        post.sp_gravity = request.POST.get('sp_gravity')
        post.ph_reaction = request.POST.get('ph_reaction')
        post.pus_cells = request.POST.get('pus_cells')
        post.rbc = request.POST.get('rbc')
        post.epi_cells = request.POST.get('epi_cells')
        post.casts = request.POST.get('casts')
        post.crystals = request.POST.get('crystals')
        post.bacteria = request.POST.get('bacteria')
        post.yeast_cells = request.POST.get('yeast_cells')
        post.trichomonas = request.POST.get('trichomonas')
        post.amorphous_deposit = request.POST.get('amorphous_deposit')
        post.albumin = request.POST.get('albumin')
        post.sugar = request.POST.get('sugar')
        post.acetone = request.POST.get('acetone')
        post.bile_pigments = request.POST.get('bile_pigments')
        post.bile_salts = request.POST.get('bile_salts')
        post.urobilinogen = request.POST.get('urobilinogen')
        post.save()
        return render(request, 'add_report_chemicalexamination.html')
    else:
        return render(request, 'add_report_chemicalexamination.html')

###################### VIEW Report Code ####################

def view_report_chemicalexamination(request):
    alldata = ChemicalExamination.objects.all()
    return render(request, 'view-report-chemicalexamination.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_report_chemicalexamination(request):
    update = ChemicalExamination.objects.get(id=id)
    update.save()
    return render(request, 'update-report-chemicalexamination.html', {"edit": update})

###################### DELETE Report Code ####################

def delete_report_chemicalexamination(request):
    delete = ChemicalExamination.objects.get(id=id)
    delete.delete()
    return redirect('/')


######################################## City #########################################

###################### ADD Report Code ####################

def add_report_city(request):
    if request.method == "POST":
        post = City()
        post.city = request.POST.get('city')
        post.city_name = request.POST.get('city_name')
        post.state = request.POST.get('state')
        post.save()
        return render(request, 'add-report-city.html')
    else:
        return render(request, 'add-report-city.html')

###################### VIEW Report Code ####################

def view_report_city(request):
    alldata = City.objects.all()
    return render(request, 'view-report-city.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_report_city(request):
    update = City.objects.get(id=id)
    update.save()
    return render(request, 'update-report-city.html', {"edit": update})

###################### DELETE Report Code ####################

def delete_report_city(request):
    delete = City.objects.get(id=id)
    delete.delete()
    return redirect('/')


######################################## Country #########################################

###################### ADD Report Code ####################

def add_report_country(request):
    if request.method == "POST":
        post = Country()
        post.country = request.POST.get('country')
        post.country_name = request.POST.get('country_name')
        post.save()
        return render(request, 'add-report-country.html')
    else:
        return render(request, 'add-report-country.html')

###################### VIEW Report Code ####################

def view_report_country(request):
    alldata = Country.objects.all()
    return render(request, 'view-report-country.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_report_country(request):
    update = Country.objects.get(id=id)
    update.save()
    return render(request, 'update-report-country.html', {"edit": update})

###################### DELETE Report Code ####################

def delete_report_country(request):
    delete = Country.objects.get(id=id)
    delete.delete()
    return redirect('/')


######################################## DiffierentialCount #########################################

###################### ADD Report Code ####################

def add_report_diffierentialcount(request):
    if request.method == "POST":
        post = DiffierentialCount()
        post.diff_count = request.POST.get('diff_count')
        post.emp_id = request.POST.get('emp_id')
        post.neutrophils = request.POST.get('neutrophils')
        post.eosinophil = request.POST.get('eosinophil')
        post.monocytes = request.POST.get('monocytes')
        post.basophil = request.POST.get('basophil')
        post.save()
        return render(request, 'add-report-diffierentialcount.html')
    else:
        return render(request, 'add-report-diffierentialcount.html')

###################### VIEW Report Code #####################

def view_report_diffierentialcount(request):
    alldata = DiffierentialCount.objects.all()
    return render(request, 'view-report-diffierentialcount.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_report_diffierentialcount(request):
    update = DiffierentialCount.objects.get(id=id)
    update.save()
    return render(request, 'update-report-diffierentialcount.html', {"edit": update})

###################### DELETE Report Code ####################

def delete_report_diffierentialcount(request):
    delete = DiffierentialCount.objects.get(id=id)
    delete.delete()
    return redirect('/')


######################################## Enquiry #########################################

###################### ADD Report Code ####################

def add_report_enquiry(request):
    if request.method == "POST":
        post = Enquiry()
        post.name = request.POST.get('name')
        post.email = request.POST.get('email')
        post.phone = request.POST.get('phone')
        post.message = request.POST.get('message')
        post.save()
        return render(request, 'add-report-enquiry.html')
    else:
        return render(request, 'add-report-enquiry.html')

###################### VIEW Report Code ####################

def view_report_enquiry(request):
    alldata = Enquiry.objects.all()
    return render(request, 'view-report-enquiry.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_report_enquiry(request):
    update = Enquiry.objects.get(id=id)
    update.save()
    return render(request, 'update-report-enquiry.html', {"edit": update})

###################### DELETE Report Code ####################

def delete_report_enquiry(request):
    delete = Enquiry.objects.get(id=id)
    delete.delete()
    return redirect('/')


######################################## State #########################################

###################### ADD Report Code ####################

def add_report_state(request):
    if request.method == "POST":
        post = State()
        post.state = request.POST.get('state')
        post.state_name = request.POST.get('state_name')
        post.country = request.POST.get('country')
        post.save()
        return render(request, 'add-report-state.html')
    else:
        return render(request, 'add-report-state.html')

###################### VIEW Report Code ####################

def view_report_state(request):
    alldata = State.objects.all()
    return render(request, 'view-report-state.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_report_state(request):
    update = State.objects.get(id=id)
    update.save()
    return render(request, 'update-report-state.html', {"edit": update})

###################### DELETE Report Code ####################

def delete_report_state(request):
    delete = State.objects.get(id=id)
    delete.delete()
    return redirect('/')


######################################## UserCompany #########################################

###################### ADD Report Code ####################

def add_report_usercompany(request):
    if request.method == "POST":
        post = UserCompany()
        post.user_company = request.POST.get('user_company')
        post.user = request.POST.get('user')
        post.company = request.POST.get('company')
        post.save()
        return render(request, 'add-report-usercompany.html')
    else:
        return render(request, 'add-report-usercompany.html')

###################### VIEW Report Code ####################

def view_report_usercompany(request):
    alldata = UserCompany.objects.all()
    return render(request, 'view-report-usercompany.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_report_usercompany(request):
    update = UserCompany.objects.get(id=id)
    update.save()
    return render(request, 'update-report-usercompany.html', {"edit": update})

###################### DELETE Report Code ####################

def delete_report_usercompany(request):
    delete = UserCompany.objects.get(id=id)
    delete.delete()
    return redirect('/')

######################################## Users #########################################

###################### ADD Report Code ####################

def add_report_users(request):
    if request.method == "POST":
        post = Users()
        post.email = request.POST.get('email')
        post.first_name = request.POST.get('first_name')
        post.last_name = request.POST.get('last_name')
        post.phone = request.POST.get('phone')
        post.photo = request.POST.get('photo')
        post.role = request.POST.get('role')
        post.password = request.POST.get('password')
        post.last_login = request.POST.get('last_login')
        post.status = request.POST.get('status')
        post.banned_users = request.POST.get('banned_users')
        post.user_com = request.POST.get('user_com')
        post.save()
        return render(request, 'add-report-users.html')
    else:
        return render(request, 'add-report-users.html')

###################### VIEW Report Code ####################


# def view_report_users(request):
#     alldata = Users.objects.all()
#     return render(request, 'view-report-users.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_report_users(request):
    update = Users.objects.get(id=id)
    update.save()
    return render(request, 'update-report-users.html', {"edit": update})

###################### DELETE Report Code ####################

def delete_report_users(request):
    delete = Users.objects.get(id=id)
    delete.delete()
    return redirect('/')




##################################################### VIEW Employee/Report Code ############################################


def view_employee_reports(request):
    alldata = EmployeeMaster.objects.all()
    return render(request, 'emp-reports.html', {'stu':alldata})


def view_summary_reports(request):
    alldata = SummaryReport.objects.all()

    return render(request, 'summary-reports.html', {'stu': alldata})


##################################################### VIEW Employee/Report Code ############################################


def reports(request):
    return render(request, 'report.html')



def final_reports(request,id):
    companyData = CompanyMaster.objects.get(id=id)
    if EmployeeMaster.objects.filter(list_company=id):
        ob = EmployeeMaster.objects.filter(list_company=id)
        contextList = []
        # context_data = {}
        # context_data['ob'] = ob
        srno = 1
        for obj in ob:
            context_data={}
            # report = {
            #     'ticket_no': obj.ticket_no,
            context_data['sr_no'] = srno
            srno += 1
            context_data['ticket_no'] = obj.ticket_no
            #     'test_date': obj.test_date,
            context_data['test_date'] = obj.test_date
            #     'employee_no': obj.employee_no,
            context_data['employee_no'] = obj.employee_no
            #     'first_name': obj.first_name,
            context_data['first_name'] = obj.first_name
            #     'designation': obj.designation,
            context_data['designation'] = obj.designation
            #     'department': obj.department,
            context_data['department'] = obj.department
            
            if obj.birthdate:
                context_data['age'] = date.today().year - obj.birthdate.year
            else:
                context_data['age'] = None
            # context[]
            # 'age': date.today().year - obj.birthdate.year,
            #     # 'object': obj
            # }
            if Hematology.objects.filter(hlogy_employee=obj.id).count() > 0:
                test = Hematology.objects.get(hlogy_employee=obj.id)
                # print(obj)
                # context_data[f'blood_group{obj.id}'] = test.blood_group
                context_data['blood_group'] = test.blood_group
                
                context_data['hemoglobin'] = test.hemoglobin
                context_data['total_wbc_count'] = test.total_wbc_count
               
            if PhysiologicalTest.objects.filter(phy_employee=obj.id).count() > 0:
                test = PhysiologicalTest.objects.get(phy_employee=obj.id)
                context_data['height'] = test.height
                context_data['weight'] = test.weight 
                context_data['remarks_and_advice'] = test.remarks_and_advice
                
                try:
                    context_data['bmi'] = (float(test.weight)/float(test.height) / float(test.height) *10000)
                    context_data['bmi'] = float(round(context_data['bmi'], 1))
                except Exception as e:
                    context_data['bmi'] = ""
               
                
                    
                        
                # context_data['bmi'] = test.height
                # height_in_meters = ((test.height) / 100)
                # context_data['bmi'] = ((test.weight) / (height_in_meters * height_in_meters))
                # height_in_meters = test.height / 100
                # context_data['bmi'] = test.weight / (height_in_meters ** 2)
                
                context_data['pulse'] = test.pulse
                context_data['blood_pressure'] = test.blood_pressure
                
            # if SystematicExamination.objects.filter(sys_employee=obj.id).count() > 0:
            #     test = SystematicExamination.objects.get(sys_employee=obj.id)

            #     context_data['ecg_context_data{obj.id}'] = test.ecg_context_data

            if BloodTest.objects.filter(btest_employee=obj.id).count() > 0:
                test = BloodTest.objects.get(btest_employee=obj.id)

                context_data['alkaline_phosphatase'] = test.alkaline_phosphatase
                context_data['blood_urea'] = test.blood_urea
                context_data['total_bilirubin'] = test.total_bilirubin
                context_data['direct_bilirubin'] = test.direct_bilirubin
                context_data['indirect_bilirubin'] = test.indirect_bilirubin
                context_data['sgot'] = test.sgot
                context_data['sgpt'] = test.sgpt
                context_data['ggt'] = test.ggt
                context_data['total_cholesterol'] = test.total_cholesterol
                context_data['triglycerides'] = test.triglycerides  
                context_data['random_blood_glucose'] = test.random_blood_glucose
                context_data['creatinine'] = test.creatinine

            if OtherTests.objects.filter(othertest_employee=obj.id).count() > 0:
                test = OtherTests.objects.get(othertest_employee=obj.id)
                context_data['serum_cholinesterase'] = test.serum_cholinesterase

            if Urine_Examination.objects.filter(urine_employee=obj.id).count() > 0:
                test = Urine_Examination.objects.get(urine_employee=obj.id)
                context_data['sugar'] = test.sugar

            if LungFunctionTest.objects.filter(lung_employee=obj.id).count() > 0:
                test = LungFunctionTest.objects.get(lung_employee=obj.id)
                print("testing")
                print(test.spirometry)
                context_data['spirometry'] = test.spirometry

            if AudiometerThresholdDecimats.objects.filter(audio_employee=obj.id).count() > 0:
                test = AudiometerThresholdDecimats.objects.get(audio_employee=obj.id)
                
                
                
            if VisualTest.objects.filter(visual_employee=obj.id).count() > 0:
                test = VisualTest.objects.get(visual_employee=obj.id)
                context_data['vision_remark'] = test.vision_remark
                
            if Complaints.objects.filter(complaints_employee=obj.id).count() > 0:
                test = Complaints.objects.get(complaints_employee=obj.id)
                context_data['personal_health_history'] = test.personal_health_history
                
            if SystematicExamination.objects.filter(sys_employee=obj.id).count() > 0:
                test = SystematicExamination.objects.get(sys_employee=obj.id)
                context_data['ecg_report'] = test.ecg_report


            # if VisualTest.objects.filter(visual_employee=obj.id).count() > 0:
            #     test = VisualTest.objects.get(visual_employee=obj.id)
            #     context_data['vision_remark'] = test.vision_remark
            #     if test.vision_remark :
            #         context_data['color_vision'] = "Accepted"  
            #     else:
            #         context_data['color_vision'] = "" 
                

            contextList.extend([context_data])
    # print(EmployeeMaster.objects.get(id=id))
            print(context_data)
            # print(context_data['ob'])
    print("now data")
    print(contextList)
    return render(request, 'final-summary-report.html', {'context':contextList, "company": companyData.name,"img":companyData.company_registration_certificate})
# , "phy": phy[0], "hlogy":hlogy[0], "sys":sys[0], "btest":btest[0], "othertest":othertest[0], "urine":urine[0], "lung":lung[0], "audio":audio[0]}

def audiometery(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
       
        # test = AudiometerThresholdDecimats.objects.get(audio_employee=obj.id)
    # obj = {
    #     'employee_no': obj.employee_no,
    #     'test_date': obj.test_date,
    #     'first_name': obj.first_name,
    #     'list_company': obj.list_company,
    #     'ticket_no' : obj.ticket_no,
    #     'birthdate' : obj.birthdate.strftime('%d/%m/%Y'),
    #     'age' : date.today().year - obj.birthdate.year,
    #     'sex' : obj.sex,
    #     # 'date_joining': obj.date_joining,
    # }    
    # if AudiometerThresholdDecimats.objects.get(audio_employee=id):
    #     obj = AudiometerThresholdDecimats.objects.get(audio_employee=id)
        
    if AudiometerThresholdDecimats.objects.filter(audio_employee=id).count() > 0:
        test = AudiometerThresholdDecimats.objects.get(audio_employee=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    obj = {
        # 'xray_report' : obj.xray_report, 
        # 'audiometery' : obj.audiometery,
        'employee_no': obj.employee_no,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'first_name': obj.first_name,
        'list_company': obj.list_company,
        'ticket_no' : obj.ticket_no,
        'birthdate' : bd,
        'age' : age,
        'sex' : obj.sex,
        'right_ac_500' : test.right_ac_500,
        'right_bc_500' : test.right_bc_500,
        'right_ac_1000': test.right_ac_1000,
        'right_bc_1000': test.right_bc_1000,
        'right_ac_2000' : test.right_ac_2000,
        'right_bc_2000' : test.right_bc_2000, 
        'right_ac_4000': test.right_ac_4000, 
        'right_bc_4000': test.right_bc_4000, 
        'right_ac_5000': test.right_ac_5000,
        'right_bc_5000': test.right_bc_5000,
        'left_ac_500' : test.left_ac_500, 
        'left_bc_500' : test.left_bc_500, 
        'left_ac_1000': test.left_ac_1000, 
        'left_bc_1000': test.left_bc_1000, 
        'left_ac_2000': test.left_ac_2000, 
        'left_bc_2000': test.left_bc_2000, 
        'left_ac_4000': test.left_ac_4000, 
        'left_bc_4000': test.left_bc_4000, 
        'left_ac_5000': test.left_ac_5000, 
        'left_bc_5000': test.left_bc_5000, 
        'for_right_ear': test.for_right_ear,
        'for_left_ear': test.for_left_ear, 
    }
    return render(request, 'AUDIOMETERY.html', {'obj': obj})


def biochemistry(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
   
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'list_company': obj.list_company,
        # 'date_joining': obj.date_joining.strftime('%d/%m/%Y'),
        'age' : age,
    }
    if OtherTests.objects.filter(othertest_employee=id).count() > 0:
        test = OtherTests.objects.get(othertest_employee=id)
        
        if test.hs_crp:
            report['hs_crp'] = float(test.hs_crp)
        else:
            report['hs_crp'] = None
        # report['status'] = 'success'

    return render(request, 'BIOCHEMISTRY.html', {'report': report})



def cholinesterase(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
    }
    if OtherTests.objects.filter(othertest_employee=id).count() > 0:
        test = OtherTests.objects.get(othertest_employee=id)
        
        if  test.serum_cholinesterase:
            report['serum_cholinesterase'] = float(test.serum_cholinesterase)
        else:
            report['serum_cholinesterase'] = None
    # if OtherTests.objects.filter(id=id):
    #     choli = OtherTests.objects.get(id=id)
    #     choli = OtherTests.objects.filter(othertest_employee=obj)
    return render(request, 'CHOLINESTERASE.html', {"report": report})
# , "phy": phy[0], "hlogy":hlogy[0], "sys":sys[0], "btest":btest[0], "othertest":othertest[0], "urine":urine[0], "lung":lung[0], "audio":audio[0]}

# def audiometery(request, id):
#     if EmployeeMaster.objects.filter(id=id):
#         obj = EmployeeMaster.objects.get(id=id)
#     report = {
#         'ticket_no': obj.ticket_no,
#         'employee_no': obj.employee_no,
#         'first_name': obj.first_name,
#         'middle_name': obj.middle_name,
#         'sex': obj.sex,
#         'birthdate': obj.birthdate,
#         'list_company': obj.list_company,
#         'date_joining': obj.date_joining,
#         'age' : date.today().year - obj.birthdate.year,
#     }
#     return render(request, 'AUDIOMETERY.html', {'obj': obj})


# def biochemistry(request, id):
#     if EmployeeMaster.objects.filter(id=id):
#         obj = EmployeeMaster.objects.get(id=id)

#     report = {
#         'employee_no': obj.employee_no,
#         'test_date': obj.test_date,
#         'first_name': obj.first_name,
#         'list_company': obj.list_company
#     }
#     if OtherTests.objects.filter(othertest_employee=id).count() > 0:
#         test = OtherTests.objects.get(othertest_employee=id)
#         report['hs_crp'] = test.hs_crp
#         # report['status'] = 'success'

#     return render(request, 'BIOCHEMISTRY.html', {'report': report})



# def cholinesterase(request, id):
#     if EmployeeMaster.objects.filter(id=id):
#         obj = EmployeeMaster.objects.get(id=id)

#     report = {
#         'ticket_no': obj.ticket_no,
#         'employee_no': obj.employee_no,
#         'first_name': obj.first_name,
#         'middle_name': obj.middle_name,
#         'sex': obj.sex,
#         'birthdate': obj.birthdate.strftime('%d/%m/%Y'),
#         'list_company': obj.list_company,
#         'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
#         'age' : date.today().year - obj.birthdate.year,
#     }
#     if OtherTests.objects.filter(othertest_employee=id).count() > 0:
#         test = OtherTests.objects.get(othertest_employee=id)
#         report['serum_cholinesterase'] = test.serum_cholinesterase
#     # if OtherTests.objects.filter(id=id):
#     #     choli = OtherTests.objects.get(id=id)
#     #     choli = OtherTests.objects.filter(othertest_employee=obj)
#     return render(request, 'CHOLINESTERASE.html', {"report": report})

# def vitamin_d3(request, id):
#     if EmployeeMaster.objects.filter(id=id):
#         obj = EmployeeMaster.objects.get(id=id)
#         btest = BloodTest.objects.filter(btest_employee=obj)
#     # if BloodTest.objects.filter(id=id):
#     #     btest = BloodTest.objects.get(id=id)
#         # btest = BloodTest.objects.filter(btest_employee=obj)
#     return render(request, 'VITAMIN-D3.html', {"obj": obj, "btest": btest})
import ast

def form_32(request, id):
    
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'collection_year':obj.collection_date.strftime('%Y'),
        'age' : age,
        'designation':obj.designation,
        'date_joining':obj.date_joining,
        'fitness_certificate_date':obj.fitness_certificate_date
    }
    if PhysiologicalTest.objects.filter(phy_employee=id).count() > 0:
        test = PhysiologicalTest.objects.get(phy_employee=id)
        report['remarks_and_advice'] = test.remarks_and_advice
    
    # companyData = CompanyMaster.objects.get(test=id)
    # if CompanyMaster.objects.filter(id=id):
    #     test = CompanyMaster.objects.get(id=id)
    #     report['test'] = test.test
        # report['test'] = ast.literal_eval(test.test)
        
    # if CompanyMaster.objects.filter(id=id).exists():
    #         companyData = CompanyMaster.objects.get(id=id)
       
    if CompanyMaster.objects.filter(id=obj.list_company.id):
        test = CompanyMaster.objects.get(id=obj.list_company.id)
        report['test'] = ast.literal_eval(test.test)
        # report['test'] = test.test
        
    
            
    return render(request, 'FORM-32.html', {'report': report})
    
def form_33(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'collection_year':obj.collection_date.strftime('%Y'),
        'fitness_certificate_date':obj.fitness_certificate_date,
        'age' : age,
    }
    if PhysiologicalTest.objects.filter(phy_employee=id).count() > 0:
        test = PhysiologicalTest.objects.get(phy_employee=id)
        report['blood_pressure'] = test.blood_pressure
        report['pulse'] = test.pulse
        
    if Complaints.objects.filter(complaints_employee=id).count() > 0:
        test = Complaints.objects.get(complaints_employee=id)
        report['id_mark_mole'] = test.id_mark_mole
    # phy = PhysiologicalTest.objects.filter(employee=obj)
    return render(request, 'FORM-33.html', {'report': report})


def form_new_o(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'collection_year':obj.collection_date.strftime('%Y'),
        'age' : age,
    }
    if PhysiologicalTest.objects.filter(phy_employee=id).count() > 0:
        test = PhysiologicalTest.objects.get(phy_employee=id)
        report['height'] = test.height
        report['weight'] = test.weight 
        report['pulse'] = test.pulse 
        report['blood_pressure'] = test.blood_pressure 
        report['heart_sound'] = test.heart_sound
        
    if VisualTest.objects.filter(visual_employee=id).count() > 0:
        test = VisualTest.objects.get(visual_employee=id)
        report['distance_vision_with_glass_right'] = test.distance_vision_with_glass_right
        report['distance_vision_with_glass'] = test.distance_vision_with_glass
        # report['distance_vision_without_glass'] = test.distance_vision_without_glass
        # report['distance_vision_without_glass_right'] = test.distance_vision_without_glass_right
        # report['nearvision_with_glass'] = test.nearvision_with_glass
        # report['nearvision_with_glass_right'] = test.nearvision_with_glass_right
        # report['distance_vision_with_glass'] = test.distance_vision_with_glass
        # report['distance_vision_with_glass_right'] = test.distance_vision_with_glass_right
        
    if BloodTest.objects.filter(btest_employee=id).count() > 0:
        test = BloodTest.objects.get(btest_employee=id)
        report['fasting_blood_glucose'] = test.fasting_blood_glucose 
        report['blood_urea'] = test.blood_urea  
        report['creatinine'] = test.creatinine
        
    return render(request, 'FORM-NEW-O.html', {"report": report})


def form_o(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'collection_year':obj.collection_date.strftime('%Y'),
        'age' : age,
    }
    if PhysiologicalTest.objects.filter(phy_employee=id).count() > 0:
        test = PhysiologicalTest.objects.get(phy_employee=id)
        report['height'] = test.height
        report['weight'] = test.weight  
        report['blood_pressure'] = test.blood_pressure  
        report['pulse'] = test.pulse
        
    if VisualTest.objects.filter(visual_employee=id).count() > 0:
        test = VisualTest.objects.get(visual_employee=id)
        report['distance_vision_with_glass_right'] = test.distance_vision_with_glass_right
        report['distance_vision_with_glass'] = test.distance_vision_with_glass
        
    if Urine_Examination.objects.filter(urine_employee=id).count() > 0:
        test = Urine_Examination.objects.get(urine_employee=id)
        report['albumin'] = test.albumin  
        report['ph_reaction'] = test.ph_reaction 
        report['sugar'] = test.sugar
        
    if SystematicExamination.objects.filter(sys_employee=id).count() > 0:
        test = SystematicExamination.objects.get(sys_employee=id)
        report['skin'] = test.skin
        
    
    if Complaints.objects.filter(complaints_employee=obj.id).count() > 0:
                test = Complaints.objects.get(complaints_employee=obj.id)
                report['id_mark_scar'] = test.id_mark_scar
                report['id_mark_mole'] = test.id_mark_mole
    
    return render(request, 'FORM-O.html', {"report": report})

def form_xi(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
    }
    return render(request, 'FORM-XI.html', {"report": report})
    

def g6pd(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
    }
    if OtherTests.objects.filter(othertest_employee=id).count() > 0:
        test = OtherTests.objects.get(othertest_employee=id)
        # if test.gppd and test.gppd.isdigit():
        report['gppd'] = (test.gppd)
        
        # report['gppd'] = float(test.gppd)

    return render(request, 'G6PD.html', {"report": report})


def hba1c(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
    }
    if OtherTests.objects.filter(othertest_employee=id).count() > 0:
        test = OtherTests.objects.get(othertest_employee=id)
        
        if test.hba1c:
            report['hba1c'] = float(test.hba1c)
        else:
            report['hba1c'] = None
            
        if test.avg_blood_glucose_level:    
            report['avg_blood_glucose_level'] = float(test.avg_blood_glucose_level)
        else:
            report['avg_blood_glucose_level'] = None
    return render(request, 'HbA1c.html', {"report": report})


def hbsag(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
    }
    if OtherTests.objects.filter(othertest_employee=id).count() > 0:
        test = OtherTests.objects.get(othertest_employee=id)
        # if  test.hbsag:    
        #     report['hbsag'] = float(test.hbsag)
        # else:
        #     report['hbsag'] = None
        report['hbsag'] = (test.hbsag)
    return render(request, 'HBSAG.html', {"report": report})

def hcv(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
    }
    if BloodTest.objects.filter(btest_employee=id).count() > 0:
        test = BloodTest.objects.get(btest_employee=id)
        # if test.hcv: 
        #     report['hcv'] = float(test.hcv)
        # else:
        #     report['hcv'] = None
        report['hcv'] = (test.hcv)
    return render(request, 'HCV.html', {"report": report})


def health_card(request, id):
    # companyData = CompanyMaster.objects.get(id=id)
    # if EmployeeMaster.objects.filter(list_company=id):
    #     ob = EmployeeMaster.objects.filter(list_company=id)
        
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
        'photo':obj.photo,
        'designation':obj.designation
    }
    if Hematology.objects.filter(hlogy_employee=id).count() > 0:
        test = Hematology.objects.get(hlogy_employee=id)
        report['blood_group'] = test.blood_group
        report['total_wbc_count'] = test.total_wbc_count
        report['esr'] = test.esr
        report['hemoglobin'] = test.hemoglobin
        report['polymorphs'] = test.polymorphs
        report['lymphocytes'] = test.lymphocytes
        report['eosinophils'] = test.eosinophils
        report['monocytes'] = test.monocytes
        report['basophils'] = test.basophils
        report['platelet_count'] = test.platelet_count

    if PhysiologicalTest.objects.filter(phy_employee=id).count() > 0:
        test = PhysiologicalTest.objects.get(phy_employee=id)
        report['height'] = test.height
        report['weight'] = test.weight
        # report['bmi'] = weight / (height * height)
        report['bmi'] = round(float(test.weight) / float(test.height) / float(test.height) * 10000)
        report['blood_pressure'] = test.blood_pressure
        
    # if PhysiologicalTest.objects.filter(phy_employee=id).count() > 0:
    #     test = PhysiologicalTest.objects.get(phy_employee=id)
    #     report['height'] = test.height
    #     report['weight'] = test.weight
    #     report['bmi'] = test.weight / (test.height * test.height)
    #     report['blood_pressure'] = test.blood_pressure


    if BloodTest.objects.filter(btest_employee=id).count() > 0:
        test = BloodTest.objects.get(btest_employee=id)
        report['random_blood_glucose'] = test.random_blood_glucose
        report['blood_cholestrol'] = test.blood_cholestrol
        report['creatinine'] = test.creatinine
        report['sgot'] = test.sgot
        report['sgpt'] = test.sgpt

    if Urine_Examination.objects.filter(urine_employee=id).count() > 0:
        test = Urine_Examination.objects.get(urine_employee=id)
        report['albumin'] = test.albumin
        report['sugar'] = test.sugar
        report['rbc'] = test.rbc
        report['crystals'] = test.crystals
        report['pus_cells'] = test.pus_cells

    if AudiometerThresholdDecimats.objects.filter(audio_employee=id).count() > 0:
        test = AudiometerThresholdDecimats.objects.get(audio_employee=id)
        report['audiometery'] = test.audiometery
        report['xray_report'] = test.xray_report

    if SystematicExamination.objects.filter(sys_employee=id).count() > 0:
        test = SystematicExamination.objects.get(sys_employee=id)
        report['ecg_report'] = test.ecg_report

    if LungFunctionTest.objects.filter(lung_employee=id).count() > 0:
        test = LungFunctionTest.objects.get(lung_employee=id)
        report['spirometry'] = test.spirometry
        
    if VisualTest.objects.filter(visual_employee=id).count() > 0:
        test = VisualTest.objects.get(visual_employee=id)
        report['nearvision_without_glass'] = test.nearvision_without_glass
        report['distance_vision_without_glass'] = test.distance_vision_without_glass
        report['nearvision_with_glass'] = test.nearvision_with_glass
        report['distance_vision_with_glass'] = test.distance_vision_with_glass
        report['nearvision_without_glass_right'] = test.nearvision_without_glass_right
        report['distance_vision_without_glass_right'] = test.distance_vision_without_glass_right
        report['nearvision_with_glass_right'] = test.nearvision_with_glass_right
        report['distance_vision_with_glass_right'] = test.distance_vision_with_glass_right
        report['vision_remark'] = test.vision_remark
        
        
    return render(request, 'Health-Card.html', {"report": report})

def hiv(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
    }
    if OtherTests.objects.filter(othertest_employee=id).count() > 0:
        test = OtherTests.objects.get(othertest_employee=id)
        report['hiv_result'] = test.hiv_result
        report['hiv_method'] = test.hiv_method
        report['hiv_remark'] = test.hiv_remark
    return render(request, 'HIV.html', {"report": report})
    


def medical(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'test_type':obj.test_type,
        'name_pref':obj.name_pref,
        'test_date': obj.test_date,
        'list_company': obj.list_company,
        'first_name': obj.first_name,
        'employee_no': obj.employee_no,
        'ticket_no': obj.ticket_no,
        'birthdate': bd,
        'designation': obj.designation,
        'department': obj.department,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age': age,
        'sex': obj.sex,
        'test_date': obj.test_date,
        'photo':obj.photo,
    }
    if PhysiologicalTest.objects.filter(phy_employee=id).count() > 0:
        test = PhysiologicalTest.objects.get(phy_employee=id)
        report['height'] = test.height
        report['weight'] = test.weight
        report['chest_on_expiration'] = test.chest_on_expiration
        report['chest_on_inspiration'] = test.chest_on_inspiration
        report['blood_pressure'] = test.blood_pressure
        report['waist'] = test.waist
        report['hips'] = test.hips
        report['pulse'] = test.pulse
        report['waist_hip_ratio'] = test.waist_hip_ratio
        report['heart_sound'] = test.heart_sound
        report['remarks_and_advice'] = test.remarks_and_advice

    if VisualTest.objects.filter(visual_employee=id).count() > 0:
        test = VisualTest.objects.get(visual_employee=id)
        report['nearvision_without_glass'] = test.nearvision_without_glass
        report['nearvision_without_glass_right'] = test.nearvision_without_glass_right
        report['distance_vision_without_glass'] = test.distance_vision_without_glass
        report['distance_vision_without_glass_right'] = test.distance_vision_without_glass_right
        report['nearvision_with_glass'] = test.nearvision_with_glass
        report['nearvision_with_glass_right'] = test.nearvision_with_glass_right
        report['distance_vision_with_glass'] = test.distance_vision_with_glass
        report['distance_vision_with_glass_right'] = test.distance_vision_with_glass_right
        report['vision_remark'] = test.vision_remark
        if test.vision_remark :
            report['color_vision'] = "Accepted"  
        else:
            report['color_vision'] = "" 
            

    if BloodTest.objects.filter(btest_employee=id).count() > 0:
        test = BloodTest.objects.get(btest_employee=id)
        
        if test.blood_cholestrol:
            report['blood_cholestrol'] = float(test.blood_cholestrol)
        else:
            report['blood_cholestrol'] = None
        
        if test.creatinine:
            report['creatinine'] = float(test.creatinine)
        else:
            report['creatinine'] = None
            
        if test.blood_urea:    
            report['blood_urea'] = float(test.blood_urea)
        else:
            report['blood_urea'] = None
        
        if test.fasting_blood_glucose:
            report['fasting_blood_glucose'] = float(test.fasting_blood_glucose)
        else:
            report['fasting_blood_glucose'] = None 
        
        if test.random_blood_glucose:    
            report['random_blood_glucose'] = float(test.random_blood_glucose)
        else:
            report['random_blood_glucose'] = None
        
        if test.post_prandial_blood_glucose:    
            report['post_prandial_blood_glucose'] = float(test.post_prandial_blood_glucose)
        else:
             report['post_prandial_blood_glucose'] = None
        
        if test.total_bilirubin:    
            report['total_bilirubin'] = float(test.total_bilirubin)
        else:
            report['total_bilirubin'] = None
        
        if  test.total_bilirubin:   
            report['direct_bilirubin'] = float(test.direct_bilirubin)
        else:
            report['direct_bilirubin'] = None
        
        if test.indirect_bilirubin :
            report['indirect_bilirubin'] = "{:.2f}".format(float(test.indirect_bilirubin))
        else:
            report['indirect_bilirubin'] = None    
        
        if test.sgpt:     
            report['sgpt'] = float(test.sgpt)   
        else:
            report['sgpt'] = None
        
        if test.sgot:   
            report['sgot'] = float(test.sgot)
        else:
            report['sgot'] = None
        
        if test.alkaline_phosphatase:  
            report['alkaline_phosphatase'] = float(test.alkaline_phosphatase)
            report['alkaline_phosphatase1'] = (test.alkaline_phosphatase)
        else:
            report['alkaline_phosphatase'] = None
        
        if test.ggt:  
            report['ggt'] = float( test.ggt)
            report['ggt1'] = (test.ggt)
        else:
            report['ggt'] = None
        
        if  test.total_cholesterol:
            report['total_cholesterol'] = float(test.total_cholesterol)
            report['total_cholesteroll'] = (test.total_cholesterol)
        else:
            report['total_cholesterol'] = None
        
        if  test.triglycerides:  
            report['triglycerides'] = float(test.triglycerides)
            report['triglycerides1'] = (test.triglycerides)
        else:
            report['triglycerides'] = None
            
        if test.direct_hdl:  
            report['direct_hdl'] = float(test.direct_hdl)
        else:
            report['direct_hdl'] = None
            
        # a = math.trunc(ldl, vldl)
        if test.vldl:
            report['vldl'] = float(test.vldl)
        else:
            report['vldl'] = None
            
        if test.ldl:    
            report['ldl'] = float( test.ldl)
        else:
            report['ldl'] = None
        
        if test.ch_ratio: 
            report['ch_ratio'] = float(test.ch_ratio)
        else:
            report['ch_ratio'] = None
        
        if test.lh_ratio: 
            report['lh_ratio'] = float(test.lh_ratio)
        else:
            report['lh_ratio'] = None
        
        report['rdw_sd'] = test.rdw_sd
        report['plcc'] = test.plcc
        report['plcr'] = test.plcr
        report['vitaminb12'] = test.vitaminb12
        report['vitamind3'] = test.vitamind3
        report['hcv'] = test.hcv
        report['psa'] = test.psa
        
        if test.bun: 
            report['bun'] = float(test.bun)
        else:
            report['bun'] = None
        ## New Code ##
        
  
        
    if SystematicExamination.objects.filter(sys_employee=id).count() > 0:
        test = SystematicExamination.objects.get(sys_employee=id)
        report['skin'] = test.skin
        report['respiratory_system'] = test.respiratory_system
        report['cardiovascular_system'] = test.cardiovascular_system
        report['genito_urinary_system'] = test.genito_urinary_system
        report['skeletal_system'] = test.skeletal_system
        report['cns'] = test.cns
        report['breath_sound'] = test.breath_sound
        report['abdomen'] = test.abdomen
        report['other_finding'] = test.other_finding
        report['ecg_report'] = test.ecg_report
    
       
    if Complaints.objects.filter(complaints_employee=id).count() > 0:
        test = Complaints.objects.get(complaints_employee=id)
        report['present_complaints'] = test.present_complaints
        report['occupational_complaints'] = test.occupational_complaints
        report['family_health_history'] = test.family_health_history
        report['personal_health_history'] = test.personal_health_history
        report['past_history'] = test.past_history
        report['allergic_to'] = test.allergic_to
        report['id_mark_scar'] = test.id_mark_scar
        report['id_mark_mole'] = test.id_mark_mole
        
        
    if Hematology.objects.filter(hlogy_employee=id).count() > 0:
        test = Hematology.objects.get(hlogy_employee=id)
        report['blood_group'] = test.blood_group
        
        if  test.hemoglobin: 
            report['hemoglobin'] = float(test.hemoglobin )
        else:
            report['hemoglobin'] = None
            
        if test.total_wbc_count:     
            report['total_wbc_count'] = int(float(test.total_wbc_count))
        else:
            report['total_wbc_count'] = None
            
        if test.total_wbc_count and test.eosinophils:
            x = float(test.total_wbc_count)
            y = float(test.eosinophils)
            report['abs'] = (x/y)

        # report['absolute'] = int(test.total_wbc_count) - int(test.eosinophils)
        if  test.polymorphs:
            report['polymorphs'] = int(float(test.polymorphs))
        else:
            report['polymorphs'] = None
        
        if test.lymphocytes:    
            report['lymphocytes'] = int(float(test.lymphocytes))
            report['lymphocytes1'] = (test.lymphocytes)
        else:
            report['lymphocytes'] = None
            
        if test.eosinophils: 
            report['eosinophils'] = int(float(test.eosinophils))
            report['eosinophils1'] =(test.eosinophils)
        else:
            report['eosinophils'] = None
        
        if test.monocytes: 
            report['monocytes'] = int(float(test.monocytes))
            report['monocytes1'] = (test.monocytes)
        else:
             report['monocytes'] = None
             
        if  test.basophils:     
            report['basophils'] = float(test.basophils)
            report['basophils1'] = (test.basophils)
        else:
            report['basophils'] = None
        
        # if 'leucocytes_count' in test.leucocytes_count:     
            report['leucocytes_count'] = test.leucocytes_count
        # else:
        #     report['leucocytes_count'] = None
            
        if test.platelet_count:         
            report['platelet_count'] = int(float(test.platelet_count))
        else:
            report['platelet_count'] = None
        
        report['esr'] = test.esr 
        
        if test.hct:         
            report['hct'] = float(test.hct )
        else:
            report['hct'] = None
            
        if test.rdw_cv:       
            report['rdw_cv'] = float(test.rdw_cv)
        else:
            report['rdw_cv'] = None
            
        if test.pdw:     
            report['pdw'] = float(test.pdw)
        else:
             report['pdw'] = None
             
        if test.mpv:    
            report['mpv'] = float(test.mpv)
        else:
            report['mpv'] = None
            
        if test.mch:     
            report['mch'] = float(test.mch)
        else:
            report['mch'] = None
            
        if test.mchc:  
            report['mchc'] = float(test.mchc)
        else:
            report['mchc'] = None
            
        if test.pct:  
            report['pct'] = float(test.pct)
        else:
            report['pct'] = None
            
        if test.mcv:  
            report['mcv'] = float(test.mcv)
        else:
            report['mcv'] = None
            
        report['peripheral_smear'] = test.peripheral_smear
        

    if AudiometerThresholdDecimats.objects.filter(audio_employee=id).count() > 0:
        test = AudiometerThresholdDecimats.objects.get(audio_employee=id)
        report['audiometery'] = test.audiometery
        report['xray_report'] = test.xray_report
        report['ultra_sonographic'] = test.ultra_sonographic

    if LungFunctionTest.objects.filter(lung_employee=id).count() > 0:
        test = LungFunctionTest.objects.get(lung_employee=id)
        report['spirometry'] = test.spirometry
        
    if Urine_Examination.objects.filter(urine_employee=id).count() > 0:
        test = Urine_Examination.objects.get(urine_employee=id)
        report['red_blood_cells'] = test.red_blood_cells
        

    if Urine_Examination.objects.filter(urine_employee=id).count() > 0:
        test = Urine_Examination.objects.get(urine_employee=id)
        report['volume'] = test.volume
        report['transparency'] = test.transparency
        report['deposit'] = test.deposit
        report['colour'] = test.colour
        report['sp_gravity'] = test.sp_gravity
        
        if test.ph_reaction: 
            report['ph_reaction'] = float(test.ph_reaction)
        else:
            report['ph_reaction'] = None
        
        report['albumin'] = test.albumin
        
        report['bile_salts'] = test.bile_salts
        report['bile_pigments'] = test.bile_pigments
        report['acetone'] = test.acetone
        report['urobilinogen'] = test.urobilinogen
        report['pus_cells'] = test.pus_cells
        report['rbc'] = test.rbc
        report['epi_cells'] = test.epi_cells
        report['casts'] = test.casts
        report['crystals'] = test.crystals
        report['bacteria'] = test.bacteria
        report['yeast_cells'] = test.yeast_cells
        report['trichomonas'] = test.trichomonas
        report['amorphous_deposit'] = test.amorphous_deposit
        report['sugar'] = test.sugar
        


    # if OtherTests.objects.filter(id=id).count() > 0:
    #     test = OtherTests.objects.get(id=id)
    #     report['stool_puscells'] = test.stool_puscells
    return render(request, 'Medical.html', {"report": report})

def medical_cert(request, id):
    # companyData = CompanyMaster.objects.get(id=id)
    # if EmployeeMaster.objects.filter(list_company=id):
    #     ob = EmployeeMaster.objects.filter(list_company=id)
        
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
        
    obj = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
        'designation': obj.designation,
       
    }

    if Complaints.objects.filter(complaints_employee=id).count() > 0:
                test = Complaints.objects.get(complaints_employee=id)
                obj['id_mark_mole'] = test.id_mark_mole
                obj['id_mark_scar'] = test.id_mark_scar
                
    if PhysiologicalTest.objects.filter(phy_employee=id).count() > 0:
                test = PhysiologicalTest.objects.get(phy_employee=id)
                obj['remarks_and_advice'] = test.remarks_and_advice
                
    # if CompanyMaster.objects.filter(id=employee_data['list_company'].id):
    #     company = CompanyMaster.objects.get(id=employee_data['list_company'].id)
    #     employee_data['address'] = company.address
    if CompanyMaster.objects.filter(id=obj['list_company'].id):
        company = CompanyMaster.objects.get(id=obj['list_company'].id)
        obj['address'] = company.address
                
    return render(request, 'Medical-cert.html', {"obj": obj})

def psa(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
    }
    if BloodTest.objects.filter(btest_employee=id).count() > 0:
        test = BloodTest.objects.get(btest_employee=id)
        if test.psa:
            report['psa'] = float(test.psa)
        else:
            report['psa'] = None
    return render(request, 'PSA.html', {"report": report})

def s_protien(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
    }
    if OtherTests.objects.filter(othertest_employee=id).count() > 0:
        test = OtherTests.objects.get(othertest_employee=id)
        if test.s_protein_total:
            report['s_protein_total'] = float(test.s_protein_total)
        else:
            report['s_protein_total'] = None
        
        if test.s_albumin_bcg:
            report['s_albumin_bcg'] = float(test.s_albumin_bcg)
        else:
            report['s_albumin_bcg'] = None
            
        if test.s_globulin:
            report['s_globulin'] = float(test.s_globulin)
        else:
            report['s_globulin'] = None
        
        if test.ag_ratio:
            report['ag_ratio'] = float(test.ag_ratio)
        else:
            report['ag_ratio'] = None
    return render(request, 'S_PROTEIN.html', {"report": report})

def sautam(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
    }
    if OtherTests.objects.filter(othertest_employee=id).count() > 0:
        test = OtherTests.objects.get(othertest_employee=id)
        report['acid_fast_bacilli'] = test.acid_fast_bacilli 
        report['stool_color'] = test.stool_color 
        report['stool_blood'] = test.stool_blood 
        report['stool_mucus'] = test.stool_mucus 
        report['stool_adults_warm'] = test.stool_adults_warm 
        report['stool_parasites'] = test.stool_parasites
        report['stool_pus'] = test.stool_pus
        report['stool_ph'] = test.stool_ph
        report['stool_occult_blood'] = test.stool_occult_blood
        report['stool_reducing_substances'] = test.stool_reducing_substances
        report['stool_rbcs'] = test.stool_rbcs
        report['stool_puscells'] = test.stool_puscells
        report['stool_fat_globules'] = test.stool_fat_globules
        report['stool_macrophages'] = test.stool_macrophages
        report['stool_epithelial_cell'] = test.stool_epithelial_cell
        report['stool_muscle_fibers'] = test.stool_muscle_fibers
        report['stool_vegetable_cell'] = test.stool_vegetable_cell
        report['stool_bacteria'] = test.stool_bacteria
        report['stool_cyst'] = test.stool_cyst
        report['stool_ova'] = test.stool_ova
        report['stool_trophozoites'] = test.stool_trophozoites
        report['stool_larva'] = test.stool_larva
        report['stool_yeast_cells'] = test.stool_yeast_cells
        report['stool_starch_granules'] = test.stool_starch_granules
    return render(request, 'SPUTAM.html', {"report": report})

def stool(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
    }
    if OtherTests.objects.filter(othertest_employee=id).count() > 0:
        test = OtherTests.objects.get(othertest_employee=id)
        report['stool_color'] = test.stool_color
        report['stool_blood'] = test.stool_blood
        report['stool_mucus'] = test.stool_mucus
        report['stool_adults_warm'] = test.stool_adults_warm
        report['stool_parasites'] = test.stool_parasites
        report['stool_pus'] = test.stool_pus
        report['stool_ph'] = test.stool_ph
        report['stool_occult_blood'] = test.stool_occult_blood
        report['stool_reducing_substances'] = test.stool_reducing_substances
        report['stool_rbcs'] = test.stool_rbcs
        report['stool_puscells'] = test.stool_puscells
        report['stool_fat_globules'] = test.stool_fat_globules
        report['stool_macrophages'] = test.stool_macrophages
        report['stool_epithelial_cell'] = test.stool_epithelial_cell
        report['stool_muscle_fibers'] = test.stool_muscle_fibers
        report['stool_vegetable_cell'] = test.stool_vegetable_cell
        report['stool_bacteria'] = test.stool_bacteria
        report['stool_cyst'] = test.stool_cyst
        report['stool_ova'] = test.stool_ova
        report['stool_trophozoites'] = test.stool_trophozoites
        report['stool_larva'] = test.stool_larva
        report['stool_yeast_cells'] = test.stool_yeast_cells
        report['stool_starch_granules'] = test.stool_starch_granules
    return render(request, 'STOOL.html', {"report": report})

def thyroid(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
    }
    if OtherTests.objects.filter(othertest_employee=id).count() > 0:
        test = OtherTests.objects.get(othertest_employee=id)
        if test.thyroid_tsh:
            report['thyroid_tsh'] = float(test.thyroid_tsh)
        else:
            report['thyroid_tsh'] = None
            
        if test.thyroid_t3:
            report['thyroid_t3'] = float(test.thyroid_t3)
        else:
            report['thyroid_t3'] = None
            
        if test.thyroid_t4:
            report['thyroid_t4'] = float(test.thyroid_t4)
        else:
            report['thyroid_t4'] = None
    return render(request, 'THYROID.html', {"report": report})

def vdrl(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
    }
    if OtherTests.objects.filter(othertest_employee=id).count() > 0:
        test = OtherTests.objects.get(othertest_employee=id)
        report['vdrl'] = test.vdrl
    return render(request, 'VDRL.html', {"report": report})

def vitamin_b12(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
    }
    if BloodTest.objects.filter(btest_employee=id).count() > 0:
        test = BloodTest.objects.get(btest_employee=id)
        if  test.vitaminb12:
            report['vitaminb12'] = float(test.vitaminb12)
        else:
            report['vitaminb12'] = None
    return render(request, 'VITAMIN-B12.html', {"report": report})

def vitamin_d3(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
    }
    if BloodTest.objects.filter(btest_employee=id).count() > 0:
        test = BloodTest.objects.get(btest_employee=id)
        if test.vitamind3:
            report['vitamind3'] = float(test.vitamind3)
        else:
            report['vitamind3'] = None
    return render(request, 'VITAMIN-D3.html', {"report": report})


# def reports(request,id):
#     pass
#     return render(request, 'profile.html', {'profile_data': obj})


# def view_employee_reports(request, id):
#     if EmployeeMaster.objects.filter(id=id):
#         obj=EmployeeMaster.objects.get(id=id)
#     return render(request, 'emp-reports.html', {'object_data':obj})


# def employee_reports(request, id):
#     if EmployeeMaster.objects.filter(id=id):
#         obj=EmployeeMaster.objects.get(id=id)
#     return render(request, 'emp-reports.html', {'report_data': obj})


def uric_ucid(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None

    report = {
        'employee_no': obj.employee_no,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'first_name': obj.first_name,
        'list_company': obj.list_company,
        'sex': obj.sex,
        'list_company': obj.list_company,
        'designation': obj.designation,
        'birthdate': bd,
        'age': age,
        'ticket_no': obj.ticket_no,
    }
    if OtherTests.objects.filter(othertest_employee=id).count() > 0:
        test = OtherTests.objects.get(othertest_employee=id)
        if test.uric_acid:
            report['uric_acid'] = float(test.uric_acid)
        else:
            report['uric_acid'] = None
        # report['status'] = 'success'

    return render(request, 'Uric.html', {'report': report})


def form_31(request, id):
    try:
        employee = EmployeeMaster.objects.get(id=id)
        companyData = employee.list_company  
        context_data = {
            'ticket_no': employee.ticket_no,
            'employee_no': employee.employee_no,
           
            'address': companyData.address if companyData else None  
        }
        
    except EmployeeMaster.DoesNotExist:
        raise Http404("EmployeeMaster matching query does not exist.")

        
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%Y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None 
        age = None
    
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date':obj.collection_date.strftime('%d/%m/%Y'),
        'age' : age,
        'address': obj.address,
    }
    if Complaints.objects.filter(complaints_employee=id).count() > 0:
        test = Complaints.objects.get(complaints_employee=id)
        report['id_mark_scar'] = test.id_mark_scar
        report['id_mark_mole'] = test.id_mark_mole
    return render(request, 'FORM_31.html', {"report": report, "company": companyData.address})


def x_ray_report(request, id):
    if EmployeeMaster.objects.filter(id=id):
        obj = EmployeeMaster.objects.get(id=id)
    if obj.birthdate:
        bd = obj.birthdate.strftime('%d/%m/%y')
        age = date.today().year - obj.birthdate.year
    else:
        bd = None
        age = None
    report = {
        'ticket_no': obj.ticket_no,
        'employee_no': obj.employee_no,
        'first_name': obj.first_name,
        'middle_name': obj.middle_name,
        'sex': obj.sex,
        'birthdate': bd,
        'list_company': obj.list_company,
        'collection_date': obj.collection_date.strftime('%d/%m/%y'),
        'age': age,
        'address': obj.address
    }

    return render(request, 'x_ray_report.html', {"report": report})







