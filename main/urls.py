from django.urls import path

from .views import ToDoCreateListView, ToDoUpdateDeleteAPIView

urlpatterns = [
    path('', ToDoCreateListView.as_view(), name='todo_create_list_view'),
    path('<int:pk>', ToDoUpdateDeleteAPIView.as_view(), name='todo_update_list_view')
]
