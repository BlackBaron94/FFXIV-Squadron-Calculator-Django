from typing import Any
from django.views.generic import (
    ListView, 
    TemplateView, 
    FormView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import SquadronMember, SquadronMissionType
from .forms import SquadronMemberForm, ChemistryForm, OptimizerForm

class HomePage(TemplateView):
    template_name = "squadron_calculator/homepage.html"

class MyCreateView(CreateView):
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs['action'] = 'Creation'
        return super().get_context_data(**kwargs)

class MyUpdateView(UpdateView):
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs['action'] = 'Update'
        return super().get_context_data(**kwargs)

# Class for Inheritance by MemberCreateView and MemberUpdateView to handle ChemistryForm
# The subclasses will need to fill in the self.object variable accordingly
class MemberFormView:
    def post(self, request, *args, **kwargs):
        print("\n\nMemberFormView POST method called\n\n")
        main_form = self.get_form()
        chemistry_form = ChemistryForm(data=request.POST)
        if not main_form.is_valid():
            return self.render_to_response(
                self.get_context_data(form=main_form, chemistry_form=chemistry_form)
            )
        # If chemistry form contains data, they are validated and saved accordingly
        # If it's empty, it's ignored and the main form is saved instead
        if chemistry_form.changed_data:
            print("\n\nChemistry Form got shit goin on\n\n")
            # If the chemistry form is invalid, the main form isn't saved
            if chemistry_form.is_valid():
                chemistry = chemistry_form.save()
                instance = main_form.save(commit=False)
                instance.chemistry = chemistry
                instance.save()
                main_form.save()
                self.object = instance
                return self.form_valid(main_form)
            else:
                return self.render_to_response(
                    self.get_context_data(form=main_form, chemistry_form=chemistry_form)
                )
        print("\n\nChemistry Form empty, no changes\n\n")
        self.object = main_form.save()
        return self.form_valid(main_form)

class MemberListView(ListView):
    template_name = "squadron_calculator/member_listview.html"
    model = SquadronMember
    queryset = SquadronMember.objects.select_related('chemistry', 'member_class', 'race')

class MemberCreateView(SuccessMessageMixin, MemberFormView, MyCreateView):
    template_name = "squadron_calculator/member_form.html"
    model = SquadronMember
    form_class = SquadronMemberForm
    success_message = "Squadron Member %(name)s added successfully!"
    success_url = reverse_lazy('members')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        if self.request.POST:
            chemistry_form = ChemistryForm(
                data=self.request.POST
            )
        else:
            chemistry_form = ChemistryForm()
        kwargs['chemistry_form'] = chemistry_form
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)

class MemberUpdateView(SuccessMessageMixin, MemberFormView, MyUpdateView):
    template_name = "squadron_calculator/member_form.html"
    model = SquadronMember
    form_class = SquadronMemberForm
    success_message = "Squadron Member %(name)s edited successfully!"
    success_url = reverse_lazy('members')
    queryset = SquadronMember.objects.select_related('chemistry')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        if self.request.POST:
            chemistry_form = ChemistryForm(
                data=self.request.POST
            )
        else:
            chemistry_form = ChemistryForm(
                instance=self.object.chemistry
            )
        kwargs['chemistry_form'] = chemistry_form
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("\n\nMemberUpdateView POST method called\n\n")
        return super().post(request, *args, **kwargs)
    
class MemberDeleteView(DeleteView):
    template_name = "squadron_calculator/member_confirm_delete.html"
    model = SquadronMember
    success_url = reverse_lazy('members')

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, f"Squadron Member {obj.name} deleted successfully!")
        return super().delete(request, *args, **kwargs)
    
class MissionListView(ListView):
    template_name = "squadron_calculator/missions.html"
    model = SquadronMissionType

class MissionDetailView(DetailView):
    template_name = "squadron_calculator/mission_type.html"
    model = SquadronMissionType
    
class Parametrics(TemplateView):
    template_name = "squadron_calculator/parametrics.html"

class MissionOptimizerView(FormView):
    template_name = "squadron_calculator/mission_optimizer.html"
    form_class = OptimizerForm
