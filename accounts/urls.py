from django.urls import path
from .views import signupview
# from config.urls import urlpatterns

urlpatterns =[
    path('signup/',signupview.as_view(), name='signup'),
]