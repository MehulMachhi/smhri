from django.urls import path
from report import views

urlpatterns = [

    path('view_employee_reports', views.view_employee_reports, name='view_employee_reports'),
    path('view_summary_reports', views.view_summary_reports, name='view_summary_reports'),
    path('final_reports/<int:id>/', views.final_reports, name='final_reports'),
    path('audiometery/<int:id>/', views.audiometery, name='audiometery'),
    path('biochemistry/<int:id>/', views.biochemistry, name='biochemistry'),
    path('cholinesterase/<int:id>/', views.cholinesterase, name='cholinesterase'),
    path('form_32/<int:id>/', views.form_32, name='form_32'),
    path('form_33/<int:id>/', views.form_33, name='form_33'),
    path('form_new_o/<int:id>/', views.form_new_o, name='form_new_o'),
    path('form_o/<int:id>/', views.form_o, name='form_o'),
    path('form_xi/<int:id>/', views.form_xi, name='form_xi'),
    path('g6pd/<int:id>/', views.g6pd, name='g6pd'),
    path('hba1c/<int:id>/', views.hba1c, name='hba1c'),
    path('hbsag/<int:id>/', views.hbsag, name='hbsag'),
    path('hcv/<int:id>/', views.hcv, name='hcv'),
    path('health_card/<int:id>/', views.health_card, name='health_card'),
    path('hiv/<int:id>/', views.hiv, name='hiv'),
    path('medical/<int:id>/', views.medical, name='medical'),
    path('medical_cert/<int:id>/', views.medical_cert, name='medical_cert'),
    path('psa/<int:id>/', views.psa, name='psa'),
    path('s_protien/<int:id>/', views.s_protien, name='s_protien'),
    path('sautam/<int:id>/', views.sautam, name='sautam'),
    path('stool/<int:id>/', views.stool, name='stool'),
    path('thyroid/<int:id>/', views.thyroid, name='thyroid'),
    path('vdrl/<int:id>/', views.vdrl, name='vdrl'),
    path('vitamin_b12/<int:id>/', views.vitamin_b12, name='vitamin_b12'),
    path('vitamin_d3/<int:id>/', views.vitamin_d3, name='vitamin_d3'),
    path('uric_ucid/<int:id>/', views.uric_ucid, name='uric_ucid'),
    path('form_31/<int:id>/', views.form_31, name='form_31'),
    path('x_ray_report/<int:id>/', views.x_ray_report, name='x_ray_report'),
    # path('emp_reports/<int:id>/', views.emp_reports, name='emp_reports'),
    # path('view_reports', views.reports, name='reports'),
    # path('add_report_appoinment', views.add_report_appointment, name='add_report_appoinment'),
    # path('view_report_appoinment', views.view_report_appointment, name='view_report_appoinment'),
    # path('update_report_appoinment/<int:id>', views.update_report_appointment, name='update_report_appoinment'),
    # path('delete_report_appoinment/<int:id>', views.delete_report_appointment, name='delete_report_appoinment'),
    #
    # path('add_report_chemicalexamination', views.add_report_chemicalexamination, name='add_report_chemicalexamination'),
    # path('view_report_chemicalexamination', views.view_report_chemicalexamination, name='view_report_chemicalexamination'),
    # path('update_report_chemicalexamination/<int:id>', views.update_report_chemicalexamination, name='update_report_chemicalexamination'),
    # path('delete_report_chemicalexamination/<int:id>', views.delete_report_chemicalexamination, name='delete_report_chemicalexamination'),
    #
    # path('add_report_city', views.add_report_city, name='add_report_city'),
    # path('view_report_city', views.view_report_city, name='view_report_city'),
    # path('update_report_city/<int:id>', views.update_report_city,name='update_report_city'),
    # path('delete_report_city/<int:id>', views.delete_report_city,name='delete_report_city'),
    #
    # path('add_report_country', views.add_report_country, name='add_report_country'),
    # path('view_report_country', views.view_report_country, name='view_report_country'),
    # path('update_report_country/<int:id>', views.update_report_country, name='update_report_country'),
    # path('delete_report_country/<int:id>', views.delete_report_country, name='delete_report_country'),
    #
    # path('add_report_diffierentialcount', views.add_report_diffierentialcount, name='add_report_diffierentialcount'),
    # path('view_report_diffierentialcount', views.view_report_diffierentialcount, name='view_report_diffierentialcount'),
    # path('update_report_diffierentialcount/<int:id>', views.update_report_diffierentialcount, name='update_report_diffierentialcount'),
    # path('delete_report_diffierentialcount/<int:id>', views.delete_report_diffierentialcount, name='delete_report_diffierentialcount'),
    #
    # path('add_report_enquiry', views.add_report_enquiry, name='add_report_enquiry'),
    # path('view_report_enquiry', views.view_report_enquiry, name='view_report_enquiry'),
    # path('update_report_enquiry/<int:id>', views.update_report_enquiry, name='update_report_enquiry'),
    # path('delete_report_enquiry/<int:id>', views.delete_report_enquiry, name='delete_report_enquiry'),
    #
    # path('add_report_state', views.add_report_state, name='add_report_state'),
    # path('view_report_state', views.view_report_state, name='view_report_state'),
    # path('update_report_state/<int:id>', views.update_report_state, name='update_report_state'),
    # path('delete_report_state/<int:id>', views.delete_report_state, name='delete_report_state'),
    #
    # path('add_report_usercompany', views.add_report_usercompany, name='add_report_usercompany'),
    # path('view_report_usercompany', views.view_report_usercompany, name='view_report_usercompany'),
    # path('update_report_usercompany/<int:id>', views.update_report_usercompany, name='update_report_usercompany'),
    # path('delete_report_usercompany/<int:id>', views.delete_report_usercompany, name='delete_report_usercompany'),
    #
    # path('add_report_users', views.add_report_users, name='add_report_users'),
    # path('view_report_users', views.view_report_users, name='view_report_users'),
    # path('update_report_users/<int:id>', views.update_report_users, name='update_report_users'),
    # path('delete_report_users/<int:id>', views.delete_report_users, name='delete_report_users'),
]



































