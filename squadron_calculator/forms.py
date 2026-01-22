from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import SquadronMember

class SquadronMemberForm(forms.ModelForm):
    model = SquadronMember

    def clean(self) -> dict[str, Any]:
        return super().clean()
    
    class Meta:
        model = SquadronMember
        fields = '__all__'