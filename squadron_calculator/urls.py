from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path("members/", views.MemberListView.as_view(), name="members"),
    path("member_creation/", views.MemberCreateView.as_view(), name="member_creation")
]