from django.urls import path
from .views import login_admin,add_course,students_schedule,schedule,destroy_schedule,update_schedule,publish_schedule,emploi_search

urlpatterns = [
    #path('',home,name='home'),
    #path('register2',register,name='register2'),
    path('add_course',add_course,name='add_course'),
    path('login_admin',login_admin,name='login_admin'),
    path('student_schedule',students_schedule,name='student_schedule'),
    path('schedule/<int:pk>',schedule,name='schedule'),
    path('schedule-delete/<int:pk>',destroy_schedule,name='destroy_schedule'),
    path('update_schedule/<int:schedule_id>',update_schedule,name='update_schedule'),
    path('publish_schedule/<int:week_num>',publish_schedule,name='publish_schedule'),
    path('emploi_search',emploi_search,name='emploi_search'),
    #path('adminitration',administration,name='administration')
]
