from django import forms
from .models import Property
from .models import Inquiry

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'property_type', 'address']



class InquiryForm(forms.ModelForm):
    phone = forms.CharField(label='Contact No', max_length=20)

    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'phone', 'message']