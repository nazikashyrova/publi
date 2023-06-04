from django.urls import path

from .views import UserDetailView, UserUpdateView, UserListView, SendFriendRequestView, FriendRequestListView, \
    FriendRequestAcceptView, FriendRequestRejectView

app_name = 'main'
urlpatterns = [
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('user/list/', UserListView.as_view(), name='user-list'),
    path('user/send-friend-request/', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('user/friend-request-list/', FriendRequestListView.as_view(), name='friend-request-list'),
    path('accept/<int:pk>/', FriendRequestAcceptView.as_view(), name='accept'),
    path('reject/<int:pk>/', FriendRequestRejectView.as_view(), name='reject'),

]
