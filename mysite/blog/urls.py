from django.urls import path

from . import views 

urlpatterns = [
    path('', views.base, name='base'),
    path('<int:post_id>/', views.detail, name='detail')
]