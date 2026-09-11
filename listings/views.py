from django.shortcuts import render, get_object_or_404
from .models import Property
from .filters import PropertyFilter
from django.contrib.auth.decorators import login_required
from .forms import PropertyForm


def property_list(request):
    property_filter = PropertyFilter(request.GET, queryset=Property.objects.all())
    return render(request, 'listings/property_list.html', {'filter': property_filter})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'listings/property_detail.html', {'property': property})

@login_required
def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.agent = request.user
            property.save()
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm()
        return render(request, 'listings/property_form.html', {'form': form})