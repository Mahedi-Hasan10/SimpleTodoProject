from django.urls import path
from todoapp.views import home,delete_todo
urlpatterns = [
    path('',home,name='homepage'),
    path('delete/<int:id>',delete_todo,name='delete')
]
