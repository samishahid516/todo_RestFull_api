from django.contrib.admin import AdminSite
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.forms import UsernameField


class EmailAdminAuthenticationForm(AdminAuthenticationForm):
    username = UsernameField(label="Email", max_length=254)


class CustomAdminSite(AdminSite):
    login_form = EmailAdminAuthenticationForm
