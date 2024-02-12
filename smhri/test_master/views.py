from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


                                                    
def get_test(request):
    return render(request, 'test.html')

from .models import (AudiometerThresholdDecimats, BloodTest, Urine_Examination, Complaints, Hematology, LungFunctionTest,
                     MicroscopicExamination, OtherTests, PhysiologicalTest, SystematicExamination, VisualTest, TestMaster)


######################################## AudiometerThresholdDecimats #########################################

###################### ADD Test Code ####################


# def add_company_data(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         pincode = request.POST.get('pincode')
#         company_registration_certificate = request.POST.get('company_registration_certificate')
#         address = request.POST.get('address')
#         country = request.POST.get('country')
#         test = request.POST.get('test')
#
#         if str('companydata')=='Yes':
#             print('in if ')
#         companydata = CompanyMaster(name=name, email=email, phone=phone, pincode=pincode,
#                                     company_registration_certificate=company_registration_certificate, address=address, country=country, test=test)
#         companydata.save()
#
#         return HttpResponseRedirect("view_company_data")
#     else:
#         return render(request, 'view-companies.html')
from employee.models import EmployeeMaster

def add_test_audiometerthresholddecimats(request, id):
    # print(id)
    
    if request.method == "POST":
        emp_id = request.POST.get('empId')
        uuser = AudiometerThresholdDecimats.objects.get(audio_employee = id)
        # audio_employee = request.POST.get('audio_employee')
        right_ac_500 = request.POST.get('right_ac_500')
        right_bc_500 = request.POST.get('right_bc_500')
        right_ac_1000 = request.POST.get('right_ac_1000')
        right_bc_1000 = request.POST.get('right_bc_1000')
        right_ac_2000 = request.POST.get('right_ac_2000')
        right_bc_2000 = request.POST.get('right_bc_2000')
        right_ac_4000 = request.POST.get('right_ac_4000')
        right_bc_4000 = request.POST.get('right_bc_4000')
        right_ac_5000 = request.POST.get('right_ac_5000')
        right_bc_5000 = request.POST.get('right_bc_5000')
        left_ac_500 = request.POST.get('left_ac_500')
        left_bc_500 = request.POST.get('left_bc_500')
        left_ac_1000 = request.POST.get('left_ac_1000')
        left_bc_1000 = request.POST.get('left_bc_1000')
        left_ac_2000 = request.POST.get('left_ac_2000')
        left_bc_2000 = request.POST.get('left_bc_2000')
        left_ac_4000 = request.POST.get('left_ac_4000')
        left_bc_4000 = request.POST.get('left_bc_4000')
        left_ac_5000 = request.POST.get('left_ac_5000')
        left_bc_5000 = request.POST.get('left_bc_5000')
        for_right_ear = request.POST.get('for_right_ear')
        for_left_ear = request.POST.get('for_left_ear')
        audiometery = request.POST.get('audiometery')
        xray_report = request.POST.get('xray_report')
        ultra_sonographic = request.POST.get('ultra_sonographic')
        # uuser = EmployeeMaster.objects.get(id=emp_id)
        print("*************************************")
        # if str('companydata') == 'Yes':
        #     print('in if ')
        companydata = AudiometerThresholdDecimats.objects.filter(audio_employee = id).update(right_ac_500=right_ac_500, right_bc_500=right_bc_500, right_ac_1000=right_ac_1000, right_bc_1000=right_bc_1000,right_ac_2000=right_ac_2000,right_bc_2000=right_bc_2000,
                            right_ac_4000=right_ac_4000, right_bc_4000=right_bc_4000, right_ac_5000=right_ac_5000, right_bc_5000=right_bc_5000, left_ac_500=left_ac_500, left_bc_500=left_bc_500, left_ac_1000=left_ac_1000,
                            left_bc_1000=left_bc_1000, left_ac_2000=left_ac_2000, left_bc_2000=left_bc_2000, left_ac_4000=left_ac_4000, left_bc_4000=left_bc_4000, left_ac_5000=left_ac_5000, left_bc_5000=left_bc_5000,
                                                  for_right_ear=for_right_ear, for_left_ear=for_left_ear, audiometery=audiometery, xray_report=xray_report, ultra_sonographic=ultra_sonographic, audio_employee = uuser)
        # companydata.save()
        # return render(request, 'profile.html')
        # return redirect(request.META['HTTP_REFERER'])
        return redirect(f"https://smhri.com/crm/profile/{id}/?next=0")
    else:
        print("#################################")
        return render(request, 'view-employees.html' )
        
        
from rest_framework.views import APIView



class post_patch_audioAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = Add_Test_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        instance = AudiometerThresholdDecimats.objects.get(pk=pk)
        serializer = Add_Test_Serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
######################################## Audiometerthresholddecimats API #########################################

class AudioAddView(generics.CreateAPIView):
    queryset = AudiometerThresholdDecimats.objects.all()
    serializer_class = AudiometerSerializer


class AudioRetUPdDestGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AudiometerThresholdDecimats.objects.all()
    serializer_class = AudiometerSerializer


###################### VIEW Report Code ####################

# def view_test_audiometerthresholddecimats(request):
#     alldata = AudiometerThresholdDecimats.objects.all()
#     return render(request, 'view-employees.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_test_audiometerthresholddecimats(request, id):
    uuser = AudiometerThresholdDecimats.objects.get(id=id)
    if request.method == "POST":
        # audio_employee = request.POST.get('audio_employee')
        right_ac_500 = request.POST.get('right_ac_500')
        right_bc_500 = request.POST.get('right_bc_500')
        right_ac_1000 = request.POST.get('right_ac_1000')
        right_bc_1000 = request.POST.get('right_bc_1000')
        right_ac_2000 = request.POST.get('right_ac_2000')
        right_bc_2000 = request.POST.get('right_bc_2000')
        right_ac_4000 = request.POST.get('right_ac_4000')
        right_bc_4000 = request.POST.get('right_bc_4000')
        right_ac_5000 = request.POST.get('right_ac_5000')
        right_bc_5000 = request.POST.get('right_bc_5000')
        left_ac_500 = request.POST.get('left_ac_500')
        left_bc_500 = request.POST.get('left_bc_500')
        left_ac_1000 = request.POST.get('left_ac_1000')
        left_bc_1000 = request.POST.get('left_bc_1000')
        left_ac_2000 = request.POST.get('left_ac_2000')
        left_bc_2000 = request.POST.get('left_bc_2000')
        left_ac_4000 = request.POST.get('left_ac_4000')
        left_bc_4000 = request.POST.get('left_bc_4000')
        left_ac_5000 = request.POST.get('left_ac_5000')
        left_bc_5000 = request.POST.get('left_bc_5000')
        for_right_ear = request.POST.get('for_right_ear')
        for_left_ear = request.POST.get('for_left_ear')
        audiometery = request.POST.get('audiometery')
        xray_report = request.POST.get('xray_report')
        ultra_sonographic = request.POST.get('ultra_sonographic')
        if str('companydata') == 'Yes':
            print('in if ')
        companydata = AudiometerThresholdDecimats(right_ac_500=right_ac_500, right_bc_500=right_bc_500, right_ac_1000=right_ac_1000, right_bc_1000=right_bc_1000,right_ac_2000=right_ac_2000,right_bc_2000=right_bc_2000,
                            right_ac_4000=right_ac_4000, right_bc_4000=right_bc_4000, right_ac_5000=right_ac_5000, right_bc_5000=right_bc_5000, left_ac_500=left_ac_500, left_bc_500=left_bc_500, left_ac_1000=left_ac_1000,
                            left_bc_1000=left_bc_1000, left_ac_2000=left_ac_2000, left_bc_2000=left_bc_2000, left_ac_4000=left_ac_4000, left_bc_4000=left_bc_4000, left_ac_5000=left_ac_5000, left_bc_5000=left_bc_5000,
                                                  for_right_ear=for_right_ear, for_left_ear=for_left_ear, audiometery=audiometery, xray_report=xray_report, ultra_sonographic=ultra_sonographic)
        companydata.save()
        # return render(request, 'profile.html')
        return redirect(request.META['HTTP_REFERER'])
    else:
        return render(request, 'view-employees.html', {'uuser': uuser})

###################### DELETE Report Code ####################

# def delete_test_audiometerthresholddecimats(request):
#     delete = AudiometerThresholdDecimats.objects.get(id=id)
#     delete.delete()
#     return redirect('/')


######################################## BloodTest #########################################

###################### ADD Test Code ######################

def add_test_bloodtest(request, id):
    if request.method == "POST":
        # emp_id = request.POST.get('empId')
        # uuser = BloodTest.objects.get(btest_employee = emp_id)
        blood_group = request.POST.get('blood_group')
        blood_cholestrol = request.POST.get('blood_cholestrol')
        creatinine = request.POST.get('creatinine')
        blood_urea = request.POST.get('blood_urea')
        fasting_blood_glucose = request.POST.get('fasting_blood_glucose')
        random_blood_glucose = request.POST.get('random_blood_glucose')
        post_prandial_blood_glucose = request.POST.get('post_prandial_blood_glucose')
        total_bilirubin = request.POST.get('total_bilirubin')
        direct_bilirubin = request.POST.get('direct_bilirubin')
        indirect_bilirubin = request.POST.get('indirect_bilirubin')
        sgpt = request.POST.get('sgpt')
        sgot = request.POST.get('sgot')
        alkaline_phosphatase = request.POST.get('alkaline_phosphatase')
        ggt = request.POST.get('ggt')
        total_cholesterol = request.POST.get('total_cholesterol')
        triglycerides = request.POST.get('triglycerides')
        direct_hdl = request.POST.get('direct_hdl')
        vldl = request.POST.get('vldl')
        ldl = request.POST.get('ldl')
        ch_ratio = request.POST.get('ch_ratio')
        lh_ratio = request.POST.get('lh_ratio')
        rdw_sd = request.POST.get('rdw_sd')
        plcc = request.POST.get('plcc')
        plcr = request.POST.get('plcr')
        vitaminb12 = request.POST.get('vitaminb12')
        vitamind3 = request.POST.get('vitamind3')
        hcv = request.POST.get('hcv')
        psa = request.POST.get('psa')
        bun = request.POST.get('bun')
        if total_bilirubin and direct_bilirubin:
            LM = float(total_bilirubin)-float(direct_bilirubin)
            
            indirect_bilirubin = format(LM, ".2f")  
        else:
            indirect_bilirubin= ""
        # if str('companydata') == 'Yes':
        #     print('in if ')
        # companydata = BloodTest(blood_cholestrol=blood_cholestrol)
        companydata = BloodTest.objects.filter(btest_employee = id).update(blood_group=blood_group,blood_cholestrol=blood_cholestrol, creatinine=creatinine, blood_urea=blood_urea, fasting_blood_glucose=fasting_blood_glucose,random_blood_glucose=random_blood_glucose,
        post_prandial_blood_glucose=post_prandial_blood_glucose,total_bilirubin=total_bilirubin, direct_bilirubin=direct_bilirubin, indirect_bilirubin=indirect_bilirubin, sgpt=sgpt, sgot=sgot, alkaline_phosphatase=alkaline_phosphatase,
        ggt=ggt, total_cholesterol=total_cholesterol, triglycerides=triglycerides, direct_hdl=direct_hdl, vldl=vldl, ldl=ldl, ch_ratio=ch_ratio, lh_ratio=lh_ratio, rdw_sd=rdw_sd, plcc=plcc, plcr=plcr, vitaminb12=vitaminb12, vitamind3=vitamind3,
        hcv=hcv,psa=psa, bun=bun)
        # companydata.save()
        # return render(request, 'view-employees.html')
        # return redirect(request.META['HTTP_REFERER'])
        return redirect(f"https://smhri.com/crm/profile/{id}/?next=1")
    else:
        return render(request, 'view-employees.html')
        
        
######################################## BloodTest API #########################################
        
class BloodTestAddView(generics.CreateAPIView):
    queryset = BloodTest.objects.all()
    serializer_class = BloodTestSerializer

class BloodTestRetUpdDesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloodTest.objects.all()
    serializer_class = BloodTestSerializer




# ###################### VIEW Report Code ####################
#
# def view_test_bloodtest(request):
#     alldata = BloodTest.objects.all()
#     return render(request, 'view-test-bloodtest.html', {'stu', alldata})
#
# ###################### UPDATE Report Code ####################
#
# def update_test_bloodtest(request):
#     update = BloodTest.objects.get(id=id)
#     update.save()
#     return render(request, 'view-test-bloodtest.html', {"edit": update})
#
# ###################### DELETE Report Code ####################
#
# def delete_test_bloodtest(request):
#     delete = BloodTest.objects.get(id=id)
#     delete.delete()
#     return redirect('/')
#
#

######################################## Urine_Examination #########################################

###################### Urine_Examination ####################

def add_urine_examination(request, id):
    if request.method == "POST":
        volume = request.POST.get('volume')
        transparency = request.POST.get('transparency')
        deposit = request.POST.get('deposit')
        colour = request.POST.get('colour')
        sp_gravity = request.POST.get('sp_gravity')
        ph_reaction = request.POST.get('ph_reaction')
        pus_cells = request.POST.get('pus_cells')
        rbc = request.POST.get('rbc')
        epi_cells = request.POST.get('epi_cells')
        casts = request.POST.get('casts')
        crystals = request.POST.get('crystals')
        bacteria = request.POST.get('bacteria')
        yeast_cells = request.POST.get('yeast_cells')
        trichomonas = request.POST.get('trichomonas')
        amorphous_deposit = request.POST.get('amorphous_deposit')
        albumin = request.POST.get('albumin')
        sugar = request.POST.get('sugar')
        acetone = request.POST.get('acetone')
        bile_pigments = request.POST.get('bile_pigments')
        bile_salts = request.POST.get('bile_salts')
        urobilinogen = request.POST.get('urobilinogen')
        
        red_blood_cells = request.POST.get('red_blood_cells')
        epithelial_cells = request.POST.get('epithelial_cells')
        urine_report = request.POST.get('urine_report')
        crystais = request.POST.get('crystais')
        material = request.POST.get('material')
        # emp_id = request.POST.get('empId')
        if str('companydata') == 'Yes':
            print('in if ')
        companydata = Urine_Examination.objects.filter(urine_employee = id).update(volume=volume, transparency=transparency, deposit=deposit, colour=colour,
                                 sp_gravity=sp_gravity, ph_reaction=ph_reaction, pus_cells=pus_cells, rbc=rbc, epi_cells=epi_cells, casts=casts, crystals=crystals, bacteria=bacteria, yeast_cells=yeast_cells, trichomonas=trichomonas,
                                 amorphous_deposit=amorphous_deposit, albumin=albumin, sugar=sugar, acetone=acetone, bile_pigments=bile_pigments, bile_salts=bile_salts, urobilinogen=urobilinogen,
                                 red_blood_cells=red_blood_cells,epithelial_cells=epithelial_cells, urine_report=urine_report,crystais=crystais, material=material)
        # companydata.save()
        # return render(request, 'view-employees.html')
        # return redirect(request.META['HTTP_REFERER'])
        return redirect(f"https://smhri.com/crm/profile/{id}/?next=2")
    else:
        return render(request, 'view-employees.html')
        
######################################## Urine API #########################################
        
        
class UrineTestAddView(generics.CreateAPIView):
    queryset = Urine_Examination.objects.all()
    serializer_class = Urine_ExaminationSerializer

class UrineTestRetUpdDesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Urine_Examination.objects.all()
    serializer_class = Urine_ExaminationSerializer


######################################## Complaints #########################################

###################### ADD Test Code ####################

def add_test_complaints(request, id):
    if request.method == "POST":
        present_complaints = request.POST.get('present_complaints')
        occupational_complaints = request.POST.get('occupational_complaints')
        family_health_history = request.POST.get('family_health_history')
        personal_health_history = request.POST.get('personal_health_history')
        past_history = request.POST.get('past_history')
        allergic_to = request.POST.get('allergic_to')
        id_mark_scar = request.POST.get('id_mark_scar')
        id_mark_mole = request.POST.get('id_mark_mole')
        # emp_id = request.POST.get('empId')
        if str('companydata') == 'Yes':
            print('in if ')
        companydata = Complaints.objects.filter(complaints_employee = id).update(present_complaints=present_complaints, occupational_complaints=occupational_complaints, family_health_history=family_health_history, personal_health_history=personal_health_history,
                                 past_history=past_history, allergic_to=allergic_to, id_mark_scar=id_mark_scar, id_mark_mole=id_mark_mole)
        # companydata.save()
        # return render(request, 'view-employees.html')
        # return redirect(request.META['HTTP_REFERER'])
        return redirect(f"https://smhri.com/crm/profile/{id}/?next=3")
    else:
        return render(request, 'view-employees.html')
        

######################################## Complains API #########################################


class CompainstAddView(generics.CreateAPIView):
    queryset = Complaints.objects.all()
    serializer_class = ComplaintsSerializer

class ComplainstRetUpdDesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Complaints.objects.all()
    serializer_class = ComplaintsSerializer


# ###################### VIEW Report Code ####################
#
# def view_test_complaints(request):
#     alldata = Complaints.objects.all()
#     return render(request, 'view-test-complaints.html', {'stu', alldata})
#
# ###################### UPDATE Report Code ####################
#
# def update_test_complaints(request):
#     update = Complaints.objects.get(id=id)
#     update.save()
#     return render(request, 'view-test-complaints.html', {"edit": update})
#
# ###################### DELETE Report Code ####################
#
# def delete_test_complaints(request):
#     delete = Complaints.objects.get(id=id)
#     delete.delete()
#     return redirect('/')
#
#
######################################## Hematology #########################################

###################### ADD Test Code ####################

def add_test_hematology(request, id):
    if request.method == "POST":
        blood_group = request.POST.get('blood_group')
        hemoglobin = request.POST.get('hemoglobin')
        total_wbc_count = request.POST.get('total_wbc_count')
        polymorphs = request.POST.get('polymorphs')
        lymphocytes = request.POST.get('lymphocytes')
        eosinophils = request.POST.get('eosinophils')
        monocytes = request.POST.get('monocytes')
        basophils = request.POST.get('basophils')
        leucocytes_count = request.POST.get('leucocytes_count')
        platelet_count = request.POST.get('platelet_count')
        esr = request.POST.get('esr')
        hct = request.POST.get('hct')
        rdw_cv = request.POST.get('rdw_cv')
        pdw = request.POST.get('pdw')
        mpv = request.POST.get('mpv')
        mch = request.POST.get('mch')
        mchc = request.POST.get('mchc')
        pct = request.POST.get('pct')
        mcv = request.POST.get('mcv')
        # emp_id = request.POST.get('empId')
        peripheral_smear = request.POST.get('peripheral_smear')
        if str('companydata') == 'Yes':
            print('in if ')
        companydata = Hematology.objects.filter(hlogy_employee = id).update(blood_group=blood_group, hemoglobin=hemoglobin, total_wbc_count=total_wbc_count, polymorphs=polymorphs, lymphocytes=lymphocytes, eosinophils=eosinophils, monocytes=monocytes,
                                 basophils=basophils, leucocytes_count=leucocytes_count, platelet_count=platelet_count, esr=esr, hct=hct, rdw_cv=rdw_cv, pdw=pdw, mpv=mpv, mch=mch, mchc=mchc, pct=pct, mcv=mcv,
                                 peripheral_smear=peripheral_smear)
        # companydata.save()
        # return render(request, 'view-employees.html')
        # return redirect(request.META['HTTP_REFERER'])
        return redirect(f"https://smhri.com/crm/profile/{id}/?next=4")
        # rerutn redirect('/crm/')
    else:
        return render(request, 'view-employees.html')
        
######################################## Hematology API #########################################
        

class HematologyAddView(generics.CreateAPIView):
    queryset = Hematology.objects.all()
    serializer_class = HematologySerializer

class HematologyRetUpdDesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hematology.objects.all()
    serializer_class = HematologySerializer


# ###################### VIEW Report Code ####################
#
# def view_test_hematology(request):
#     alldata = Hematology.objects.all()
#     return render(request, 'view-test-hematology.html', {'stu', alldata})
#
# ###################### UPDATE Report Code ####################
#
# def update_test_hematology(request):
#     update = Hematology.objects.get(id=id)
#     update.save()
#     return render(request, 'view-test-hematology.html', {"edit": update})
#
# ###################### DELETE Report Code ####################
#
# def delete_test_hematology(request):
#     delete = Hematology.objects.get(id=id)
#     delete.delete()
#     return redirect('/')
#
#
######################################## LungFunctionTest #########################################

###################### ADD Test Code ####################

def add_test_lungfunctiontest(request, id):
    if request.method == "POST":
        fvc = request.POST.get('fvc')
        fev1 = request.POST.get('fev1')
        fev1_fvc = request.POST.get('fev1_fvc')
        peak_exp_flow = request.POST.get('peak_exp_flow')
        fef50 = request.POST.get('fef50')
        fvc_predicted = request.POST.get('fvc_predicted')
        fev1_predicted = request.POST.get('fev1_predicted')
        fev1_fvc_predicted = request.POST.get('fev1_fvc_predicted')
        pefr_predicted = request.POST.get('pefr_predicted')
        fef50_predicted = request.POST.get('fef50_predicted')
        fvc_per_predicted = request.POST.get('fvc_per_predicted')
        fev1_per_predicted = request.POST.get('fev1_per_predicted')
        fev1_fvc_per_predicted = request.POST.get('fev1_fvc_per_predicted')
        pefr_per_predicted = request.POST.get('pefr_per_predicted')
        fef50_per_predicted = request.POST.get('fef50_per_predicted')
        spirometry = request.POST.get('spirometry')
        # emp_id = request.POST.get('empId')
        companydata = LungFunctionTest.objects.filter(lung_employee = id).update(fvc=fvc, fev1=fev1, fev1_fvc=fev1_fvc,peak_exp_flow=peak_exp_flow, fef50=fef50, fvc_predicted=fvc_predicted,fev1_predicted=fev1_predicted,
                                 fev1_fvc_predicted=fev1_fvc_predicted, pefr_predicted=pefr_predicted, fef50_predicted=fef50_predicted,fvc_per_predicted=fvc_per_predicted,
                                 fev1_per_predicted=fev1_per_predicted, fev1_fvc_per_predicted=fev1_fvc_per_predicted, pefr_per_predicted=pefr_per_predicted,
                                 fef50_per_predicted=fef50_per_predicted, spirometry=spirometry)
        # companydata.save()
        # return redirect(request.META['HTTP_REFERER'])
        return redirect(f"https://smhri.com/crm/profile/{id}/?next=5")
        # return redirect('/crm/view_employees_data')    
    else:
        return render(request, 'view-employees.html')

######################################## LungFunctionTest  API #########################################


class LungFunctionAddView(generics.CreateAPIView):
    queryset = LungFunctionTest.objects.all()
    serializer_class = LungFunctionTestSerializer

class LungFunctionTestRetUpdDesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LungFunctionTest.objects.all()
    serializer_class = LungFunctionTestSerializer


# ###################### VIEW Report Code ####################
#
# def view_test_lungfunctiontest(request):
#     alldata = LungFunctionTest.objects.all()
#     return render(request, 'view-test-lungfunctiontest.html', {'stu', alldata})
#
# ###################### UPDATE Report Code ####################
#
# def update_test_lungfunctiontest(request):
#     update = LungFunctionTest.objects.get(id=id)
#     update.save()
#     return render(request, 'view-test-lungfunctiontest.html', {"edit": update})
#
# ###################### DELETE Report Code ####################
#
# def delete_test_lungfunctiontest(request):
#     delete = LungFunctionTest.objects.get(id=id)
#     delete.delete()
#     return redirect('/')
#
#
######################################## MicroscopicExamination #########################################


# req.user.id = userid
from django.urls import reverse

###################### ADD Test Code ####################

def add_test_microscopicexamination(request, id):
    if request.method == "POST":
        red_blood_cells = request.POST.get('red_blood_cells')
        pus_cells = request.POST.get('pus_cells')
        epithelial_cells = request.POST.get('epithelial_cells')
        urine_report = request.POST.get('urine_report')
        casts = request.POST.get('casts')
        crystais = request.POST.get('crystais')
        material = request.POST.get('material')
        # emp_id = request.POST.get('empId')
        companydata = MicroscopicExamination.objects.filter(micro_employee = id).update(red_blood_cells=red_blood_cells, pus_cells=pus_cells, epithelial_cells=epithelial_cells, urine_report=urine_report, casts=casts,
                                       crystais=crystais, material=material)
        # companydata.save()
        # return render(request, 'view-employees.html')
        # return redirect(reverse('profile', kwargs={'id':id}))    
        # return redirect(request.META['HTTP_REFERER'])
        return redirect(f"https://smhri.com/crm/profile/{id}/?next=6")
    else:
        return render(request, 'view-employees.html')

######################################## MicroscopicExamination API #########################################

class MicroAddview(generics.CreateAPIView):
    queryset = MicroscopicExamination.objects.all()
    serializer_class = MicroscopicExaminationSerializers

class MicroRetUpaDesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MicroscopicExamination.objects.all()
    serializer_class = MicroscopicExaminationSerializers


# ###################### VIEW Report Code ####################
#
# def view_test_microscopicexamination(request):
#     alldata = MicroscopicExamination.objects.all()
#     return render(request, 'view-test-microscopicexamination.html', {'stu', alldata})
#
# ###################### UPDATE Report Code ####################
#
# def update_test_microscopicexamination(request):
#     update = MicroscopicExamination.objects.get(id=id)
#     update.save()
#     return render(request, 'view-test-microscopicexamination.html', {"edit": update})
#
# ###################### DELETE Report Code ####################
#
# def delete_test_microscopicexamination(request):
#     delete = MicroscopicExamination.objects.get(id=id)
#     delete.delete()
#     return redirect('/')
#
#
######################################## OtherTests #########################################

###################### ADD Test Code ####################

def add_test_othertests(request, id):
    if request.method == "POST":
        serum_cholinesterase = request.POST.get('serum_cholinesterase')
        uric_acid = request.POST.get('uric_acid')
        hs_crp = request.POST.get('hs_crp')
        gppd = request.POST.get('gppd')
        hba1c = request.POST.get('hba1c')
        avg_blood_glucose_level = request.POST.get('avg_blood_glucose_level')
        hbsag = request.POST.get('hbsag')
        hiv_result = request.POST.get('hiv_result')
        hiv_method = request.POST.get('hiv_method')
        hiv_remark = request.POST.get('hiv_remark')
        s_protein_total = request.POST.get('s_protein_total')
        s_albumin_bcg = request.POST.get('s_albumin_bcg')
        s_globulin = request.POST.get('s_globulin')
        ag_ratio = request.POST.get('ag_ratio')
        acid_fast_bacilli = request.POST.get('acid_fast_bacilli')
        stool_color = request.POST.get('stool_color')
        stool_blood = request.POST.get('stool_blood')
        stool_mucus = request.POST.get('stool_mucus')
        stool_adults_warm = request.POST.get('stool_adults_warm')
        stool_parasites = request.POST.get('stool_parasites')
        stool_pus = request.POST.get('stool_pus')
        stool_ph = request.POST.get('stool_ph')
        stool_occult_blood = request.POST.get('stool_occult_blood')
        stool_reducing_substances = request.POST.get('stool_reducing_substances')
        stool_rbcs = request.POST.get('stool_rbcs')
        stool_puscells = request.POST.get('stool_puscells')
        stool_fat_globules = request.POST.get('stool_fat_globules')
        stool_macrophages = request.POST.get('stool_macrophages')
        stool_epithelial_cell = request.POST.get('stool_epithelial_cell')
        stool_muscle_fibers = request.POST.get('stool_muscle_fibers')
        stool_vegetable_cell = request.POST.get('stool_vegetable_cell')
        stool_bacteria = request.POST.get('stool_bacteria')
        stool_cyst = request.POST.get('stool_cyst')
        stool_ova = request.POST.get('stool_ova')
        stool_trophozoites = request.POST.get('stool_trophozoites')
        stool_larva = request.POST.get('stool_larva')
        stool_yeast_cells = request.POST.get('stool_yeast_cells')
        stool_starch_granules = request.POST.get('stool_starch_granules')
        thyroid_tsh = request.POST.get('thyroid_tsh')
        thyroid_t3 = request.POST.get('thyroid_t3')
        thyroid_t4 = request.POST.get('thyroid_t4')
        vdrl = request.POST.get('vdrl')
        # emp_id = request.POST.get('empId')
        companydata = OtherTests.objects.filter(othertest_employee = id).update(uric_acid=uric_acid, serum_cholinesterase=serum_cholinesterase, hs_crp=hs_crp,gppd=gppd, hba1c=hba1c, avg_blood_glucose_level=avg_blood_glucose_level,hbsag=hbsag, hiv_result=hiv_result,
                 hiv_method=hiv_method, hiv_remark=hiv_remark, s_protein_total=s_protein_total, s_albumin_bcg=s_albumin_bcg, s_globulin=s_globulin, ag_ratio=ag_ratio, acid_fast_bacilli=acid_fast_bacilli,
                 stool_color=stool_color, stool_blood=stool_blood, stool_mucus=stool_mucus, stool_adults_warm=stool_adults_warm, stool_parasites=stool_parasites, stool_pus=stool_pus,stool_ph=stool_ph,
                 stool_occult_blood=stool_occult_blood, stool_reducing_substances=stool_reducing_substances, stool_rbcs=stool_rbcs, stool_puscells=stool_puscells, stool_fat_globules=stool_fat_globules,stool_macrophages=stool_macrophages,
                 stool_epithelial_cell=stool_epithelial_cell, stool_muscle_fibers=stool_muscle_fibers,stool_vegetable_cell=stool_vegetable_cell, stool_bacteria=stool_bacteria, stool_cyst=stool_cyst,
                 stool_ova=stool_ova, stool_trophozoites=stool_trophozoites, stool_larva=stool_larva, stool_yeast_cells=stool_yeast_cells, stool_starch_granules=stool_starch_granules, thyroid_tsh=thyroid_tsh,
                 thyroid_t3=thyroid_t3, thyroid_t4=thyroid_t4, vdrl=vdrl)
        # companydata.save()
        return redirect(request.META['HTTP_REFERER'])
        # return redirect("https://smhri.com/crm/profile/" id")
        # return redirect('/crm/view_employees_data')    
    else:
        return render(request, 'view-employees.html')

######################################## OtherTests API #########################################


class OthertestsAddView(generics.CreateAPIView):
    queryset = OtherTests.objects.all()
    serializer_class = OtherTestsSerializers

class OthertestsRetUpdDesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OtherTests.objects.all()
    serializer_class = OtherTestsSerializers


# ###################### VIEW Report Code ####################
#
# def view_test_othertests(request):
#     alldata = OtherTests.objects.all()
#     return render(request, 'view-test-othertests.html', {'stu', alldata})
#
# ###################### UPDATE Report Code ####################
#
# def update_test_othertests(request):
#     update = OtherTests.objects.get(id=id)
#     update.save()
#     return render(request, 'view-test-othertests.html', {"edit": update})
#
# ###################### DELETE Report Code ####################
#
# def delete_test_othertests(request):
#     delete = OtherTests.objects.get(id=id)
#     delete.delete()
#     return redirect('/')
#
#
######################################## PhysiologicalTest #########################################

###################### ADD Test Code ####################

def add_test_physiologicaltest(request, id):
    if request.method == "POST":
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        blood_pressure = request.POST.get('blood_pressure')
        pulse = request.POST.get('pulse')
        heart_sound = request.POST.get('heart_sound')
        chest_on_expiration = request.POST.get('chest_on_expiration')
        chest_on_inspiration = request.POST.get('chest_on_inspiration')
        waist = request.POST.get('waist')
        hips = request.POST.get('hips')
        waist_hip_ratio = request.POST.get('waist_hip_ratio')
        remarks_and_advice = request.POST.get('remarks_and_advice')
        # emp_id = request.POST.get('empId')
        companydata = PhysiologicalTest.objects.filter(phy_employee = id).update(height=height, weight=weight, blood_pressure=blood_pressure, pulse=pulse, heart_sound=heart_sound, chest_on_expiration=chest_on_expiration,
                                         chest_on_inspiration=chest_on_inspiration, waist=waist, hips=hips, waist_hip_ratio=waist_hip_ratio, remarks_and_advice=remarks_and_advice)
        # companydata.save()
        # return redirect(request.META['HTTP_REFERER'])
        return redirect(f"https://smhri.com/crm/profile/{id}/?next=7")
        # return redirect('/crm/view_employees_data')    
    else:
        return render(request, 'view-employees.html')
        
######################################## PhysiologicalTest API #########################################


class PhysiologicalTestAddView(generics.CreateAPIView):
    queryset = PhysiologicalTest.objects.all()
    serializer_class = PhysiologicalTestSerializer


class PhysiologicalTestRetUpdDesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhysiologicalTest.objects.all()
    serializer_class = PhysiologicalTestSerializer


# ###################### VIEW Report Code ####################
#
# def view_test_physiologicaltest(request):
#     alldata = PhysiologicalTest.objects.all()
#     return render(request, 'view-test-physiologicaltest.html', {'stu', alldata})
#
# ###################### UPDATE Report Code ####################
#
# def update_test_physiologicaltest(request):
#     update = PhysiologicalTest.objects.get(id=id)
#     update.save()
#     return render(request, 'view-test-physiologicaltest.html', {"edit": update})
#
# ###################### DELETE Report Code ####################
#
# def delete_test_physiologicaltest(request):
#     delete = PhysiologicalTest.objects.get(id=id)
#     delete.delete()
#     return redirect('/')
#
#
######################################## SystematicExamination #########################################

################### ADD Test Code #######################

def add_test_systematicexamination(request, id):
    if request.method == "POST":
        skin = request.POST.get('skin')
        respiratory_system = request.POST.get('respiratory_system')
        cardiovascular_system = request.POST.get('cardiovascular_system')
        genito_urinary_system = request.POST.get('genito_urinary_system')
        skeletal_system = request.POST.get('skeletal_system')
        cns = request.POST.get('cns')
        breath_sound = request.POST.get('breath_sound')
        abdomen = request.POST.get('abdomen')
        other_finding = request.POST.get('other_finding')
        ecg_report = request.POST.get('ecg_report')
        # emp_id = request.POST.get('empId')
        companydata = SystematicExamination.objects.filter(sys_employee = id).update(skin=skin, respiratory_system=respiratory_system, cardiovascular_system=cardiovascular_system, genito_urinary_system=genito_urinary_system,
                                        skeletal_system=skeletal_system, cns=cns,breath_sound=breath_sound, abdomen=abdomen, other_finding=other_finding,
                                        ecg_report=ecg_report)
        # companydata.save()
        # return redirect(request.META['HTTP_REFERER'])
        return redirect(f"https://smhri.com/crm/profile/{id}/?next=8")
        # return redirect('/crm/view_employees_data')
    else:
        return render(request, 'view-employees.html')

######################################## SystematicExamination API #########################################


class SystematicExaminationAddView(generics.CreateAPIView):
    queryset = SystematicExamination.objects.all()
    serializer_class = SystematicExaminationSerializers

class SystematicExaminationRetUpdDesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SystematicExamination.objects.all()
    serializer_class = SystematicExaminationSerializers


# ###################### VIEW Report Code ####################
#
# def view_test_systematicexamination(request):
#     alldata = SystematicExamination.objects.all()
#     return render(request, 'view-test-systematicexamination.html', {'stu', alldata})
#
# ###################### UPDATE Report Code ####################
#
# def update_test_systematicexamination(request):
#     update = SystematicExamination.objects.get(id=id)
#     update.save()
#     return render(request, 'view-test-systematicexamination.html', {"edit": update})
#
# ###################### DELETE Report Code ####################
#
# def delete_test_systematicexamination(request):
#     delete = SystematicExamination.objects.get(id=id)
#     delete.delete()
#     return redirect('/')
#
#
######################################## VisualTest #########################################

###################### ADD Test Code ####################

def add_test_visualtest(request, id):
    if request.method == "POST":
        nearvision_without_glass = request.POST.get('nearvision_without_glass')
        distance_vision_without_glass = request.POST.get('distance_vision_without_glass')
        nearvision_with_glass = request.POST.get('nearvision_with_glass')
        distance_vision_with_glass = request.POST.get('distance_vision_with_glass')
        nearvision_without_glass_right = request.POST.get('nearvision_without_glass_right')
        distance_vision_without_glass_right = request.POST.get('distance_vision_without_glass_right')
        nearvision_with_glass_right = request.POST.get('nearvision_with_glass_right')
        distance_vision_with_glass_right = request.POST.get('distance_vision_with_glass_right')
        vision_remark = request.POST.get('vision_remark')
        # emp_id = request.POST.get('empId')
        companydata = VisualTest.objects.filter(visual_employee = id).update(nearvision_without_glass=nearvision_without_glass, distance_vision_without_glass=distance_vision_without_glass,nearvision_with_glass=nearvision_with_glass,
                        distance_vision_with_glass=distance_vision_with_glass,nearvision_without_glass_right=nearvision_without_glass_right, distance_vision_without_glass_right=distance_vision_without_glass_right,
                        nearvision_with_glass_right=nearvision_with_glass_right,distance_vision_with_glass_right=distance_vision_with_glass_right, vision_remark=vision_remark,
                                            )
        # companydata.save()
        # return redirect(request.META['HTTP_REFERER'])
        return redirect(f"https://smhri.com/crm/profile/{id}/?next=9")
        # return redirect('/crm/view_employees_data') 
    else:
        return render(request, 'view-employees.html')
        
######################################## VisualTest API #########################################


class VisualTestAddView(generics.CreateAPIView):
    queryset = VisualTest.objects.all()
    serializer_class = VisualTestSerializers

class VisualTestRetUpdDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = VisualTest.objects.all()
    serializer_class = VisualTestSerializers

# ###################### VIEW Report Code ####################
#
# def view_test_visualtest(request):
#     alldata = VisualTest.objects.all()
#     return render(request, 'view-test-visualtest.html', {'stu', alldata})
#
# ###################### UPDATE Report Code ####################
#
# def update_test_visualtest(request):
#     update = VisualTest.objects.get(id=id)
#     update.save()
#     return render(request, 'view-test-visualtest.html', {"edit": update})
#
# ###################### DELETE Report Code ####################
#
# def delete_test_visualtest(request):
#     delete = VisualTest.objects.get(id=id)
#     delete.delete()
#     return redirect('/')
#
#
# ######################################## TestMaster #########################################
#
# ###################### ADD Test Code ####################
#
# def add_test_testmaster(request):
#     if request.method == "POST":
#         post = TestMaster()
#         post.test_id = request.POST.get('test_id')
#         post.test_name = request.POST.get('test_name')
#         post.test_desc = request.POST.get('test_desc')
#         post.status = request.POST.get('status')
#         post.test_model = request.POST.get('test_model')
#         post.save()
#         return render(request, 'add-test-testmaster.html')
#     else:
#         return render(request, 'add-test-testmaster.html')
#
# ###################### VIEW Report Code ####################
#
# def view_test_testmaster(request):
#     alldata = TestMaster.objects.all()
#     return render(request, 'view-test-testmaster.html', {'stu', alldata})
#
# ###################### UPDATE Report Code ####################
#
# def update_test_testmaster(request):
#     update = TestMaster.objects.get(id=id)
#     update.save()
#     return render(request, 'view-test-testmaster.html', {"edit": update})
#
# ###################### DELETE Report Code ####################
#
# def delete_test_testmaster(request):
#     delete = TestMaster.objects.get(id=id)
#     delete.delete()
#     return redirect('/')




















