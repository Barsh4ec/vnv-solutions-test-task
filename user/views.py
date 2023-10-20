from django.urls import reverse_lazy
from django.views import generic

from user.forms import UsersCreationForm, GroupForm, UsersUpdateForm
from user.models import User, Group


class UserListView(generic.ListView):
    model = User
    queryset = User.objects.prefetch_related("groups")


class DriverCreateView(generic.CreateView):
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


class GroupCreateView(generic.CreateView):
    model = Group
    form_class = GroupForm
    success_url = reverse_lazy("user:group-list")

    def form_valid(self, form):
        group = form.save()
        selected_users = form.cleaned_data.get("users")
        group.users.set(selected_users)

        return super().form_valid(form)
