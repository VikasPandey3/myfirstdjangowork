from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,Iot
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    UserAdmin.fieldsets += ('API', {'fields': ('api_key',)}),
    model = CustomUser
    add_fieldsets = (
        (None,
         {'classes': ('wide',),
          'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',)
          }
         ),
    )
    list_display = ['username',]


admin.site.register(CustomUser, CustomUserAdmin,)
admin.site.register(Iot)

