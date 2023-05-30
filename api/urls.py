from django.urls import path
from .views import UserListCreate, UserRetrieve

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieve.as_view(), name='user-detail'),
]
