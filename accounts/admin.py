from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustoumUserCreationForm,CustoumUserChangeForm
from .models import CustomUser
# Register your models here.
class CustoumUserAdmin(UserAdmin):
    add_form = CustoumUserCreationForm
    form = CustoumUserChangeForm
    model=CustomUser
    list_display = [
        'email',
        'username',
        'age',
        'is_staff'
    ]

    fieldsets = UserAdmin.fieldsets+((None,{"fields":('age',)}),)
    add_fieldsets = UserAdmin.add_fieldsets+((None,{"fields":('age',)}),)

admin.site.register(CustomUser, CustoumUserAdmin)
