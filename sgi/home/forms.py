from django.contrib.auth.forms import (
    AuthenticationForm, 
    UsernameField
)
from django.utils.translation import gettext, gettext_lazy as _
from django import forms


class SGI_AuthenticationForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': _('Username')
        }))

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _("Password")
        }),
    )
