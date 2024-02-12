from django.urls import path
from company import views



from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
# , ResetPasswordView, ChangePasswordView
from .forms import LoginForm
# from .views import  profile
# home,, RegisterView
from .views import CustomLoginView
# , ResetPasswordView, ChangePasswordView

urlpatterns = [
    path('', views.index, name="index"),
    path('add_company_data', views.add_company_data, name='add_company_data'),
    path('view_company_data', views.view_company_data, name='view_company_data'),
    path('edit_company_data/<int:id>', views.edit_company_data, name='edit_company_data'),
    path('update_company_data/<int:id>/', views.update_company_data, name='update_company_data'),
    path('delete_company_data/<int:id>/', views.delete_company_data, name='delete_company_data'),
    
    
    
    # path('admin/', admin.site.urls),
    # path('profile/', profile, name='profile'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('login_view', views.login_view, name='login_view'),
    # path('home', views.home, name='home')

]