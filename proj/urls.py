"""defines url patterns for todo list"""

from django.urls import path

from . import views

app_name = 'proj'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # Page shows all tasks
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]