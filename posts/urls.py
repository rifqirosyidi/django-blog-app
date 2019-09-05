from django.urls import path, include
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.post_list),
    path('<int:id>/', views.post_detail, name='detail'),
    path('create/', views.post_create),
    path('update/', views.post_update),
    path('delete/', views.post_delete),
]
