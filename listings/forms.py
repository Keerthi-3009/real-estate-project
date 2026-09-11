from django import forms
from .models import Property, Inquiry, SellerSubmission, SellerSubmissionImage
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'property_type', 'address']



class InquiryForm(forms.ModelForm):
    phone = forms.CharField(label='Contact No', max_length=20)

    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'phone', 'message']

class SellerSubmissionForm(forms.ModelForm):
    class Meta:
        model = SellerSubmission
        fields = [
            'name',
            'email',
            'phone',
            'property_title',
            'description',
            'address',
            'price',
        ]


class SellerSubmissionImageForm(forms.ModelForm):
    class Meta:
        model = SellerSubmissionImage
        fields = ['image']