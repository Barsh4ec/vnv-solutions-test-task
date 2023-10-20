from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from user.models import User, Group


class UsersCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "password1", "password2", "groups")


class UsersUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "groups")


class GroupForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.SelectMultiple
    )

    class Meta:
        model = Group
        fields = "__all__"
