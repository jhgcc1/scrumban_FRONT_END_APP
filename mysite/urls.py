"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from polls import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth import login , urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('about/', views.about, name='about'),
    url(r'^login/$', views.login, name="login"),
    url(r'^register/$', views.register, name="register"),
    url(r'^password_reset/$', PasswordResetView.as_view(template_name='forgotpassword.html',email_template_name='emailfgtpassword.html',subject_template_name='subjectemailfgtpassword.html'), name='ps'),
    url(r'^password_reset/done/$',PasswordResetDoneView.as_view(template_name='passwordresetsent.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',PasswordResetConfirmView.as_view(template_name='forgotpassword2.html'), name='password_reset_confirm'),
    url(r'^reset/done/$', PasswordResetCompleteView.as_view(template_name='forgotpassword3.html'), name='password_reset_complete'),
   ]