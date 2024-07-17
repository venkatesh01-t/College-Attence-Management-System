from django.urls import path

from .views import *
from . import views


urlpatterns = [
     path('ven/',ven,name='venkatesh'),
     path('', views.login, name='login'),
     path('mainpage/', mainpage, name='principal_page'),
     path('home/', views.home, name='home'),
     path('mainpanal/', mainpanal, name='mainpanal'),
     path('view/<str:year>', view, name='view'),
     path('viewall/', viewpage, name='viewall'),
     path('studentlogin/', student_login, name='student_login'),
     path('student_view/<str:key>', student_view, name='student_view'),
     path('searchviewpage/', searchviewpage, name='searchviewpage'),
     path('attencemainpage/', reattence, name='attence_main_page'),
     path('attencetake/<str:year>', attences_take, name='attencetake'),
     path('student_details/<str:year>',create_details,name='student_details'),
     path('student_deleteug/<int:id>',create_deleteug,name='student_deleteug'),
     path('student_deletepg/<int:id>',create_deletepg,name='student_deletepg'),
     path('edit_student/<int:id>',edit_student,name='edit_student'),
     path('delete_student/<int:id>',delete_student,name='delete_student'),
    # path('add_student/', views.add_student, name='add_student'),
    # path('student_list/', views.student_list, name='student_list'),

]
