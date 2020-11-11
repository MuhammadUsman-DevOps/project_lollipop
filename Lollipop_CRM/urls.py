

from django.contrib import admin
from django.urls import path

from Lollipop_CRM import views

urlpatterns = [
    path('accounts/login/', views.auth_login, name="Login"),
    path('logout', views.auth_logout, name="Logout"),
    path('add/customer/', views.add_customer, name="Add Customer"),
    path('view/customer/', views.view_customer, name="View Customer"),
    path('create/package/', views.create_package, name="Create Package"),
    path('package/label/<str:package_number>/', views.package_label, name="Package Label"),
    path('view/packages/', views.view_package, name="View Package"),
]
