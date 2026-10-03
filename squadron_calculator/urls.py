from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path("members/", views.MemberListView.as_view(), name="members"),
    path("member-create/", views.MemberCreateView.as_view(), name="member_creation"),
    path("member-update/<int:pk>/", views.MemberUpdateView.as_view(), name="member_update"),
    path("member-delete/<int:pk>/", views.MemberDeleteView.as_view(), name="member_delete"),
    path("missions/", views.MissionListView.as_view(), name="missions"),
    path("mission-type/<int:pk>/", views.MissionDetailView.as_view(), name="mission_type"),
    path("parametrics/", views.Parametrics.as_view(), name="parametrics"),
    path("mission-optimizer/", views.MissionOptimizerView.as_view(), name="mission_optimizer"),
]