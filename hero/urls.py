from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    url(r'^employees/$', views.EmployeesCreate.as_view(), name='employee-list'),
    path('username/<username>/', views.UsernameList.as_view(),
         name='username-list'),
    path('enterprise/<enterprise>', views.EmployeesList.as_view(),
         name='enterprise-list'),

]
