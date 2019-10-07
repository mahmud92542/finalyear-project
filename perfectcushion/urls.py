"""perfectcushion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as authViews
from django.contrib import admin
from django.urls import path, include
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('shop/', include('shop.urls')),
    path('search/', include('search_app.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('account/create/', views.signupView, name='signup'),
    path('account/login/', views.signinView, name='signin'),
    path('account/logout/', views.signoutView, name='signout'),
    #This path will request the customer to type in the email address he or she wants to receive the new instructions to reset the password
    path('account/password-reset/',
    authViews.PasswordResetView.as_view(template_name='accounts/reset_password.html'),
    name='password_reset'),
 
#This will inform the customer a new email has been sent with the instruction
    path('account/password-reset/done/',
     authViews.PasswordResetDoneView.as_view(template_name='accounts/reset_password_done.html'),
     name='password_reset_done'),
 
#This path will provide a specific url with a base64 hash as well as with a token
    path('account/password-reset-confirm/<uidb64>/<token>/',
     authViews.PasswordResetConfirmView.as_view(template_name='accounts/reset_password_confirm.html'),
     name='password_reset_confirm'),
 
#This will inform the customer that the password has been changed
    path('account/password-reset-complete/',
     authViews.PasswordResetCompleteView.as_view(template_name='accounts/reset_password_complete.html'),
     name='password_reset_complete'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)