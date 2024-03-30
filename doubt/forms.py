from django import forms
from .models import Doubt,Solution

class DoubtForm(forms.ModelForm):
    class Meta:
        model = Doubt
        fields = ['subject', 'description']  # Fields to include in the form
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),  # Textarea widget with 4 rows
        }

class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['description']  # Fields that you want to include in the form