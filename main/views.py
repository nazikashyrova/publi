from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, FormView, UpdateView, ListView
from accounts.models import User, FriendshipRequest
from main.forms import FriendRequestForm

class UserListView(ListView):
    model = User
    template_name = 'main/user_list.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return User.objects.filter(
                Q(username__icontains=query) |
                Q(full_name__icontains=query)
            )
        return User.objects.all()

class UserDetailView(DetailView):
    model = User
    template_name = 'main/user_detail.html'
    context_object_name = 'user'

class UserUpdateView(UpdateView):
    model = User
    template_name = 'main/user_update.html'
    fields = ['first_name', 'last_name', 'biography', 'profile_image']


class SendFriendRequestView(FormView):
    template_name = 'send_friend_request.html'
    form_class = FriendRequestForm
    success_url = '/user/list/'  # Redirect to the user list page after sending the friend request

    def form_valid(self, form):
        return super().form_valid(form)

class FriendRequestListView(View):
    def get(self, request):
        friend_requests = FriendshipRequest.objects.filter(receiver=request.user)
        return render(request, 'main/list.html', {'friend_requests': friend_requests})

class FriendRequestAcceptView(View):
    def post(self, request, pk):
        friend_request = FriendshipRequest.objects.get(pk=pk)
        friend_request.status = 'accepted'
        friend_request.save()
        # Additional logic to create chat room and perform other actions
        return redirect('main:friend-request-list')

class FriendRequestRejectView(View):
    def post(self, request, pk):
        friend_request = FriendshipRequest.objects.get(pk=pk)
        friend_request.status = 'rejected'
        friend_request.save()
        return redirect('main:friend-request-list')