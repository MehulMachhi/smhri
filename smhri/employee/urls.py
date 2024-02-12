from django.urls import path
from employee import views

urlpatterns = [
    path('add_employees_data', views.add_employees_data, name='add_employees_data'),
    path('view_employees_data', views.view_employees_data, name='view_employees_data'),
    # path('edit_employees_data', views.edit_employees_data, name='edit_employees_data'),
    
    # Change comment
    path('update_employees_data/<int:id>', views.update_employees_data, name='update_employees_data'),
    
    path('delete_employees_data/<int:id>', views.delete_employees_data, name='delete_employees_data'),
    # path('view_employees_data', views.view_employees_data, name='view_employees_data'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('audiometery1', views.audiometery1, name='audiometery1'),
    path('biochemistry', views.biochemistry, name='biochemistry')
]