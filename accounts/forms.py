from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustoumUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields=UserCreationForm.Meta.fields +('age',)
class CustoumUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=UserChangeForm.Meta.fields