from typing import Any
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, CreateView
from .models import SquadronMember
from .forms import SquadronMemberForm

class HomePage(TemplateView):
    template_name = "squadron_calculator/homepage.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)


class MemberListView(ListView):
    template_name = "squadron_calculator/member_listview.html"
    model = SquadronMember

class MemberCreateView(CreateView):
    template_name = "squadron_calculator/member_createview.html"
    model = SquadronMember
    form_class = SquadronMemberForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        print(ctx)
        return ctx