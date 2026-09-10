from django.shortcuts import render, get_object_or_404
from .models import Property
from .filters import PropertyFilter

def property_list(request):
    property_filter = PropertyFilter(request.GET, queryset=Property.objects.all())
    return render(request, 'listings/property_list.html', {'filter': property_filter})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'listings/property_detail.html', {'property': property})