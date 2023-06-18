from django.template.context_processors import static
from django.urls import path

from publi import settings
from . import views
app_name = 'posts'
urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('<int:pk>/save/', views.SavePost.as_view(), name='save_post'),
]