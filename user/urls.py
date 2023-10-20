from django.urls import path

from user.views import (
    UserListView,
    DriverCreateView,
    GroupListView,
    GroupCreateView,
    UserUpdateView,
    UserDeleteView
)


urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/create/", DriverCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/update/", UserUpdateView.as_view(), name="user-update"),
    path("users/<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),
    path("groups/", GroupListView.as_view(), name="group-list"),
    path("group/create/", GroupCreateView.as_view(), name="group-create"),
]

app_name = "user"
