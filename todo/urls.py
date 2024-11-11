from django.urls import path
from todo.views import index, remove, edit

urlpatterns = [
    path('', index, name='todo'),
    path('del/<int:id>', remove),
    path('edit/<int:id>', edit),
]
