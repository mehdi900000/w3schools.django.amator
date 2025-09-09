from django.urls import path
from .views import PostListView,PostCreate,PostDetail,PostUpdate,PostDelete


urlpatterns=[
        path('',PostListView.as_view(),name='home'),
        path('post/',PostCreate.as_view(), name='create'),
        path('post/<int:pk>/',PostDetail.as_view(), name='detail'),
        path('post/<int:pk>/edit/',PostUpdate.as_view(), name='update'),
        path('post/<int:pk>/delete/',PostDelete.as_view(), name='delete')
]