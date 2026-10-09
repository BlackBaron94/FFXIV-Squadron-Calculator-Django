from django import forms
from .models import SquadronMember, Chemistry, SquadronMission

class BaseForm(forms.Form):
    start_group: list[str] | str = []
    break_group: list[str] | str = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Sets Bootstrap class "form-control" for most elements 
        # (Checkboxes and RadioSelects excluded)
        for _, field in self.fields.items():
            if not isinstance(field, forms.BooleanField) and \
            not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs['class'] = 'form-control'
        # Sets the break/start_group attributes for formation of HTML
        if self.start_group == '__all__' and self.break_group == '__all__':
            for field in self.visible_fields():
                setattr(field, 'start_group', True)
                setattr(field, 'break_group', True)
            return
        for field in self.visible_fields():
            if field.name in self.start_group:
                setattr(field, 'start_group', True)
            if field.name in self.break_group:
                setattr(field, 'break_group', True)

class SquadronMemberForm(BaseForm, forms.ModelForm):
    start_group = ['name', 'physical_stat', 'member_class']
    break_group = ['name', 'tactical_stat', 'level']
    
    class Meta:
        model = SquadronMember
        exclude = ('chemistry', )
        
class ChemistryForm(BaseForm, forms.ModelForm):
    start_group = '__all__'
    break_group = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if self.changed_data:
            for field in self.visible_fields():
                if cleaned_data.get(field.name) in ('', None):
                    self.add_error(
                        field.name, 
                        f"Field '{field.label}' is required \
                            when submitting a Chemistry."
                    )
        return cleaned_data

    class Meta:
        model = Chemistry
        fields = '__all__'
        widgets = {'priority': forms.RadioSelect}

class SquadronMissionForm(BaseForm, forms.ModelForm):
    start_group = ['mission_type', 'required_physical']
    break_group = ['mission_type', 'required_tactical']

    class Meta:
        model = SquadronMission
        exclude = ('success_chance_message',)