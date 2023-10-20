from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from user.forms import UsersCreationForm, GroupForm, UsersUpdateForm
from user.models import User, Group


def index(request):

    return render(request, "index.html")


class UserListView(generic.ListView):
    model = User
    queryset = User.objects.prefetch_related("groups")
    paginate_by = 5


class UserCreateView(generic.CreateView):
    model = User
    form_class = UsersCreationForm
    success_url = reverse_lazy("user:user-list")


class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UsersUpdateForm
    success_url = reverse_lazy("user:user-list")


class UserDeleteView(generic.DeleteView):
    model = User
    success_url = reverse_lazy("user:user-list")


class GroupListView(generic.ListView):
    model = Group
    queryset = Group.objects.prefetch_related("users")
    paginate_by = 5


class GroupCreateView(generic.CreateView):
    model = Group
    form_class = GroupForm
    success_url = reverse_lazy("user:group-list")


class GroupUpdateView(generic.UpdateView):
    model = Group
    form_class = GroupForm
    success_url = reverse_lazy("user:group-list")


class GroupDeleteView(generic.DeleteView):
    model = Group
    success_url = reverse_lazy("user:group-list")
