from django import forms
from .models import ScannerHistory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset,ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class ScannerForm(forms.Form):

  
    class Meta:
        model = ScannerHistory
        fields = [
            'target',
            'type'
        ]

    target = forms.CharField(
        required=True,
        max_length=20,
        min_length=7,
        strip=True
    )

    
    QUICK = 'QS'
    FULL = 'FS'
    type = forms.ChoiceField(
        choices = (
            (QUICK, "Quick scan"),
            (FULL, "Full scan")
        ),
        widget = forms.RadioSelect,
        initial = 'QS',
    )

