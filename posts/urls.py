from django.urls import path, include
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.post_list, name='list'),
    path('<int:id>/', views.post_detail, name='detail'),
    path('create/', views.post_create),
    path('<int:id>/update/', views.post_update),
    path('<int:id>/delete/', views.post_delete),
]
