from django import forms
from django.utils.translation import ugettext_lazy as _
from sights.models import Sight, Jellyfish


class SightReportForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Sight
        fields = ['date', 'jellyfish', 'jellyfish_size', 'jellyfish_quantity',
                  'description', 'description_extra', 'address', 'lat', 'lng',
                  'image_name', 'image'
                  ]
        widgets = {
            'address': forms.TextInput(attrs={'size': 100}),
            'lat': forms.TextInput(attrs={'size': 10}),
            'lng': forms.TextInput(attrs={'size': 10}),
            'image_name': forms.TextInput(attrs={'size': 50}),
        }