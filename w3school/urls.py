from django.urls import path
from .views import messageview


urlpatterns =[
    path('',messageview.as_view(),name='w3school')
]


