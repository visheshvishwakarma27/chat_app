
from django.urls import path
from core import views
from chat import views as chat_views

from .views import *
from .form import MyChangePasswordForm , PasswordResetForm
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView


urlpatterns =[
    path('', home, name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
   
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('Logout/',LogoutView.as_view(next_page='/Login/'), name='Logout'),
    path('change_password/', PasswordChangeView.as_view(template_name="core/change_password.html", form_class=MyChangePasswordForm), name='change_password'),
    path('password-change-done/', PasswordChangeDoneView.as_view(template_name="core/password-change-done.html"), name="password_change_done"),
    path('reset-password/', PasswordResetView.as_view(template_name='core/reset-password.html', form_class= PasswordResetForm), name='reset-password'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('chathome', chat_views.chathome, name="chathome"),
    path('<str:room>/', chat_views.room, name="room"),
    path('checkview', chat_views.checkview, name="checkview"),
    path('send', chat_views.send, name="send"),
    path('getMessages/<str:room>/', chat_views.getMessages, name="getMessages")

]


