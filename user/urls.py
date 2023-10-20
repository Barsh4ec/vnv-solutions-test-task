from django.urls import path

from user.views import (
    UserListView,
    UserCreateView,
    GroupListView,
    GroupCreateView,
    UserUpdateView,
    UserDeleteView,
    GroupUpdateView,
    GroupDeleteView
)


urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/create/", UserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/update/", UserUpdateView.as_view(), name="user-update"),
    path("users/<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),
    path("groups/", GroupListView.as_view(), name="group-list"),
    path("group/create/", GroupCreateView.as_view(), name="group-create"),
    path("group/<int:pk>/update/", GroupUpdateView.as_view(), name="group-update"),
    path("group/<int:pk>/delete/", GroupDeleteView.as_view(), name="group-delete"),
]

app_name = "user"
