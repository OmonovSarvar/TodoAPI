from django.urls import path

from drftestapp1.views import TodoList, TodoCreate, TodoDetail, TodoUpdate, TodoDelete

urlpatterns = [
    path('api/', TodoList.as_view()),
    path('api/new', TodoCreate.as_view()),
    path('api/<int:id>', TodoDetail.as_view()),
    path('api/<int:id>/delete', TodoDelete.as_view()),
    path('api/<int:id>/update', TodoUpdate.as_view())
]
