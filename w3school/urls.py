from django.urls import path
from .views import messageview
# from config.urls import urlpatterns



urlpatterns=[
    path('', messageview.as_view(), name='message'),
]
