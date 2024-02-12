from django.shortcuts import render, HttpResponse, redirect
from .models import CompanyMaster
from django.http import HttpResponseRedirect
from report.models import SummaryReport
from employee.models import EmployeeMaster
from django.contrib.auth.decorators import login_required
# Create your views here.

######################  INDEX PAGE ########################

@login_required
def index(request):
    return render(request, 'index.html')

###################### Add Company Data ####################

# def add_company_data(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         print('mehul')
#         city = request.POST.get('city')
#         company_type = request.POST.get('company_type')
#         company_registration_certificate = request.POST.get('company_registration_certificate')
#         CompanyMaster.objects.create(name=name, phone=phone, email=email, address=address,
#                                            city=city, company_type=company_type, company_registration_certificate=company_registration_certificate)
#         company_master = CompanyMaster.objects.all()
#         return render(request, 'add-company.html', {'stu': company_master})
#     else:
#         company_master = CompanyMaster.objects.all()
#         return render(request, 'add-company.html', {'stu': company_master})

# def add_company_data(request):
#
#     if request.POST.get('name')  and request.POST.get('phone') and request.POST.get(
#                  'email') and request.POST.get('address') and request.POST.get('city') and request.POST.get(
#                  'company_type') and request.POST.get('company_registration_certificate'):
#                     app = CompanyMaster()
#                     app.name = request.POST.get('name')
#                     app.phone = request.POST.get('phone')
#                     app.email = request.POST.get('email')
#                     app.address = request.POST.get('address')
#                     app.city = request.POST.get('city')
#                     app.company_type = request.POST.get('company_type')
#                     app.company_registration_certificate = request.POST.get('company_registration_certificate'):
#
#                     app.name = request.POST.get('name')
#                     app.save()
#                     print('mehul')
#                     company_master = CompanyMaster.objects.all()
#                     return render(request, 'add-company.html', {'stu': company_master})
#     else:
#
#             company_master = CompanyMaster.objects.all()
#             return render(request, 'add-company.html', {'stu': company_master})


# def add_company_data(request):
#     if request.method == "POST":
#         print('zzz')
#         if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('address') and request.POST.get('city') and request.POST.get('company_type') and request.POST.get('company_registration_certificate'):
#
#             app = CompanyMaster()
#
#             app.name = request.POST.get('name')
#             app.phone = request.POST.get('phone')
#             app.email = request.POST.get('email')
#             app.address = request.POST.get('address')
#             app.city = request.POST.get('city')
#             app.company_type = request.POST.get('company_type')
#             app.company_registration_certificate = request.POST.get('company_registration_certificate')
#             app.save()
#             master = CompanyMaster.objects.all()
#             return render(request, 'add-company.html', {'stu': master})
#
#     else:
#
#         master = CompanyMaster.objects.all()
#         return render(request, 'add-company.html', {'stu': master})
#
# def add_company_data(request):
#     if request.method == "POST":
#         post = CompanyMaster()
#         post.name = request.POST.get('name')
#         post.email = request.POST.get('email')
#         post.phone = request.POST.get('phone')
#         post.pincode = request.POST.get('pincode')
#         post.company_registration_certificate = request.POST.get('company_registration_certificate')
#         post.address = request.POST.get('address')
#         post.country = request.POST.get('country')
#         post.test = request.POST.get('test')
#         post.save()
#         alldata = CompanyMaster.objects.all()
#         return render(request, 'view-companies.html', {"stu": alldata})
#     else:
#         return render(request, 'view-companies.html')


def add_company_data(request):
    if request.method == 'POST':
        tests = []
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        company_registration_certificate = request.POST.get('company_registration_certificate')
        address = request.POST.get('address')
        country = request.POST.get('country')
        test = request.POST.getlist('test[]')
        testArr = []
        if not isinstance(test, list):
            testArr.append(test)
        else :
            testArr = test
        # if len(test) == 1:
        #     test = [test]
        # print("test:::",test)

        if str('companydata')=='Yes':
            print('in if ')
        companydata = CompanyMaster(name=name, email=email, phone=phone, pincode=pincode,
                                    company_registration_certificate=company_registration_certificate, address=address, country=country, test=testArr)
        companydata.save()
        SummaryReport.objects.create(company_name=companydata, )

        return HttpResponseRedirect("view_company_data")
    else:
        return render(request, 'view-companies.html')

###################### GET Company Data ####################

def view_company_data(request):
        alldata = CompanyMaster.objects.all()
        return render(request, 'view-companies.html', {"stu": alldata})

###################### EDIT Company Code ####################

def edit_company_data(request, id):
    alldata = CompanyMaster.objects.get(id=id)
    return render(request, 'update-companies.html', {"stu": alldata})

###################### UPDATE Company Code ###################

# def update_company_data(request, id):
#     data = CompanyMaster.objects.get(id=id)
#     if request.method == "POST":
#         print('update chale che................')
#         data = CompanyMaster()
#         # post.id = request.POST.get('id')
#         data.name = request.POST.get('name')
#         data.email = request.POST.get('email')
#         data.phone = request.POST.get('phone')
#         data.pincode = request.POST.get('pincode')
#         data.company_registration_certificate = request.POST.get('company_registration_certificate')
#         data.address = request.POST.get('address')
#         data.country = request.POST.get('country')
#         data.test = request.POST.get('test')
#         data.save()
#         return redirect('view_company_data')
#     else:
#         post = CompanyMaster.objects.get(id=id)
#         return render(request, 'update-companies.html', {"stu": post})

def update_company_data(request, id):
    uuser = CompanyMaster.objects.get(id=id)
    vuser = CompanyMaster.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        company_registration_certificate = request.POST.get('company_registration_certificate')
        address = request.POST.get('address')
        country = request.POST.get('country')
        test = request.POST.getlist('test[]')
        testArr = []
        if not isinstance(test, list):
            test = [test]
        CompanyMaster.objects.filter(pk=id).update(name=name, email=email, phone=phone, pincode=pincode,
                                    company_registration_certificate=company_registration_certificate, address=address, country=country, test=test)
        # return render(request, 'view-companies.html', {'vuser': vuser})
        return redirect('/crm/view_company_data')
    else:
        uuser = CompanyMaster.objects.get(id=id)
        return render(request,'update-companies.html',{'uuser': uuser})
    
###################### DELETE Company Code ####################

def delete_company_data(request, id):
    delete = CompanyMaster.objects.get(id=id)
    delete.delete()
    return redirect('/crm')
    
    
    
    
########################################## Login Page View ########################################



from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm



# @login_required
# def profile(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return render(request, 'index.html')
            
#             # return render(request, 'index.html')
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateProfileForm(instance=request.user.profile)
    
#     return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        
        # def get_success_url:
        #     return reverse_lazy("smhri/crm")
            
        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)
            
            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)
        
    

    
# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect

def login_view(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('index')
    #     else:
    #         error_message = 'Invalid username or password.'
    #         return render(request, 'index.html', {'error_message': error_message})
    # else:
    #     return render(request, 'index.html')
    return render(request, 'login.html')

def home(request):
    form_class = LoginForm
        
        
    return redirect('home')


















