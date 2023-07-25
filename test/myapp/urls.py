from django.urls import path
from . import views
from myapp.views import *
urlpatterns = [
    path('', views.home, name='home'),
    path('employee/<int:id>/', views.employee, name='employee'),
    path('delete-employee/<int:id>/', views.delete_employee, name="delete_employee"),
    path('update-employee/<int:id>/', views.update_employee, name="update_employee"),
    
    
    path('login/',login_page,name = "login_page"),
    path('register/', register, name='register_page'),
    path('logout/', logout_page , name ="logout_page"),
    
    # owner
    path('owner/<id>/', owner , name = 'owner'),
    path('delete-owner/<id>/', delete_owner, name='delete_owner'),
    path('update-owner/<id>', update_owner, name='update_owner'),
 
  #company
    path('company/', company, name="company"),
    path('delete-company/<id>/', delete_company, name="delete_company"),
    path('update-company/<id>/', update_company, name="update_company"),
    
    
  

    path('intern/<int:id>/', views.intern, name='intern'),
    path('delete-intern/<id>/', delete_intern, name="delete_intern"),
    path('update-intern/<id>/', update_intern, name="update_intern"),

]
