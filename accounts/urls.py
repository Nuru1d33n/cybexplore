from django.urls import path, include
from accounts.views import RegisterView

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', RegisterView, name="register"),
    # path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/', include('allauth.urls')),

    # path("accounts/password_reset/", auth_views.PasswordResetView.as_view(template_name="registration/password_resetForm.html"), name="password_reset"),
    # path("accounts/password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="registration/password_resetConfirm.html"), name="password_reset_done"),
    # path("accounts/reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_confirm"),
    # path("accounts/reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_complete"),
]

