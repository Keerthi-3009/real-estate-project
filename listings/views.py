from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import BuyerInquiryForm
from django.contrib import messages
from .models import SellerSubmission, SellerSubmissionImage

from .models import (
    Property,
    PropertyImage,
    Inquiry,
    SellerSubmissionImage
)

from .filters import PropertyFilter

from .forms import (
    PropertyForm,
    InquiryForm,
    SellerSubmissionForm
)

def is_agent(user):
    return user.is_authenticated and user.role == 'agent'

def property_list(request):
    property_filter = PropertyFilter(request.GET, queryset=Property.objects.all())
    return render(request, 'listings/property_list.html', {'filter': property_filter})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'listings/property_detail.html', {'property': property})




@login_required
def property_create(request):
    if request.user.role != 'agent':
        return redirect('property_list')
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.agent = request.user
            property.save()

            images = request.FILES.getlist('images')
            for img in images:
                PropertyImage.objects.create(property=property, image=img)

            messages.success(request, "Property added successfully!")
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm()
    return render(request, 'listings/property_form.html', {'form': form})
@login_required
def property_edit(request, pk):
    property = get_object_or_404(
        Property,
        pk=pk,
        agent=request.user
    )

    if request.method == 'POST':
        form = PropertyForm(
            request.POST,
            instance=property
        )

        if form.is_valid():
            form.save()

            # Get newly uploaded images
            images = request.FILES.getlist('images')

            # Save each new image
            for img in images:
                PropertyImage.objects.create(
                    property=property,
                    image=img
                )

            return redirect(
                'property_detail',
                pk=property.pk
            )

    else:
        form = PropertyForm(instance=property)

    return render(
        request,
        'listings/property_form.html',
        {
            'form': form,
            'editing': True,
            'property': property
        }
    )
@login_required
def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk, agent=request.user)
    if request.method == 'POST':
        property.delete()
        return redirect('property_list')
    return render(request, 'listings/property_confirm_delete.html', {'property': property})



def property_inquiry(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.property = property
            inquiry.save()
            return redirect('property_detail', pk=property.pk)
    else:
        form = InquiryForm()
    return render(request, 'listings/property_inquiry.html', {'form': form, 'property': property})




def sell_property(request):
    if request.method == 'POST':
        form = SellerSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save()

            images = request.FILES.getlist('images')
            for img in images:
                SellerSubmissionImage.objects.create(submission=submission, image=img)

            messages.success(request, "Your property details were submitted successfully! An agent will contact you soon.")
            return redirect('property_list')
    else:
        form = SellerSubmissionForm()
    return render(request, 'listings/sell_property.html', {'form': form})

def is_agent(user):
    return user.is_authenticated and user.role == 'agent'



def buyer_signup(request):
    if request.method == 'POST':
        form = BuyerInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! Your requirements were submitted successfully. An agent will reach out to you soon.")
            return redirect('property_list')
    else:
        form = BuyerInquiryForm()
    return render(request, 'listings/buyer_signup.html', {'form': form})