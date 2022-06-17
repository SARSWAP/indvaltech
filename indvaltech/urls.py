from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
     path('', views.login_user, name='login'),
     path('dashboard/', views.dashboard, name="dashboard"),
     path('register/<str:name>/', views.register, name="register"),
     path('family/<str:name>/', views.family, name="family"),
     path('hr/', views.hr, name="hr"),
     path('documents/<str:name>/', views.documents, name="documents"),
     path('bank/<str:name>/', views.bank, name="bank"),
     path('AddProject/',AddProject.as_view(), name='AddProject'),
     path('AddProject/<pk>/',AddProject.as_view(), name='AddProject'),
     path('AttendForm/',views.AttendForm, name='AttendForm'),
     path('sheets/', views.timesheet, name='sheets'),
     path('DesignDashboard/',views.DesignDashboard, name='DesignDashboard'),
     path('education/<str:name>/',views.education, name='education'),
     path('history/<str:name>/', views.history, name='history'),
     path('AddActivity/',AddActivity.as_view(), name='AddActivity'),
     path('AddActivity/<pk>/',AddActivity.as_view(), name='AddActivity'),
     path('leave/', views.leave, name='leave'),
     path('payslip', views.payslip, name="payslip"),
     path('hrd', views.hrd, name="hrd"),
     path('reset/', ResetPasswordView.as_view(), name="reset"),
      path('education', views.education, name="education"),
]
