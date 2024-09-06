from django.urls import path
from .views import *


urlpatterns = [
    path('users/', User_all.as_view()),
    path('create/', User_create.as_view()),
    path('put/', User_put.as_view()),
    path('delet/<int:id>/', User_delete.as_view()),
    path('put/', User_put.as_view()),
]