from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CostumUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CostumUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'address', 'job']

admin.site.register(CustomUser, CustomUserAdmin)