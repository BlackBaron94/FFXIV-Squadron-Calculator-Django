from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import SquadronMember, Chemistry, SquadronMissionType, SquadronMission

class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            if not isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-control'

class SquadronMemberForm(BaseForm, forms.ModelForm):
    model = SquadronMember
    
    class Meta:
        model = SquadronMember
        exclude = ('chemistry', )
        
class ChemistryForm(BaseForm, forms.ModelForm):
    model = Chemistry

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            if field.label.lower() == 'priority':
                field.widget.attrs['class'] = ''
            field.required = False

    def clean(self):
        cleaned_data = super().clean()
        if self.changed_data:
            if cleaned_data.get('bonus') == '':
                self.add_error('bonus', 'Το πεδίο Bonus είναι υποχρεωτικό εφόσον συμπληρώνετε Chemistry.')
            
            if not cleaned_data.get('condition_proc'):
                self.add_error('condition_proc', 'Το πεδίο Condition είναι υποχρεωτικό.')

            if not cleaned_data.get('reward_type'):
                self.add_error('reward_type', 'Το πεδίο Reward Type είναι υποχρεωτικό.')

            if cleaned_data.get('priority') == '':
                self.add_error('priority', 'Το πεδίο Priority είναι υποχρεωτικό.')

        return cleaned_data

    class Meta:
        model = Chemistry
        fields = '__all__'
        widgets = {'priority': forms.RadioSelect}

class OptimizerForm(BaseForm, forms.ModelForm):
    class Meta:
        model = SquadronMission
        exclude = ('success_chance_message',)
