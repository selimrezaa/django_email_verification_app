from django.contrib import admin
from django.urls import path
from first_app import views


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.sign_up, name='signup'),
    #email varifications
    path('password-reset/', views.PasswordResetView.as_view(template_name='first_app/passwordreset.html'), name='password_reset'),
    path('password-reset-done/', views.PasswordResetDoneView.as_view(template_name='first_app/passwordresetdone.html'), name='password_reset_done'),
    path('rest/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='first_app/passwordresetconfirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', views.PasswordResetCompleteView.as_view(template_name='first_app/passwordresetcomplete.html'), name='password_reset_complete'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
