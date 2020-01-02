from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('ask/', views.ask, name = 'ask'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
   	path('edit/', views.edit, name='edit'),
   	path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', views.index, name='post_list_by_tag'),
]