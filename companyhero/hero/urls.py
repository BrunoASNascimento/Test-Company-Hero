from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^employees/$', views.EmployeesList.as_view(), name='employee-list'),

]
