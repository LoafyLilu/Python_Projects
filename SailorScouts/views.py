from django.shortcuts import render, redirect, get_object_or_404
from .forms import ScoutForm
from .models import Scout


# Create your views here.

# Story 1 - Build the basic App
def sailorscouts_home(request):
    return render(request, 'SailorScouts/SailorScouts_home.html')

# Story 2 - Create model and add entry
def sailorscouts_add(request):
    form = ScoutForm(data=request.POST or None)
    if request.method == 'POST':
        # returns user to home page
        if form.is_valid():  # Checks to see if the submitted form is valid, and saves if so.
            form.save()
            return redirect('sailorscouts_list')  # returns user to home page

        # Saves the content to the template as a dictionary, and adds content of form to page
    content = {'form': form}
    return render(request, 'SailorScouts/SailorScouts_add.html', content)

# Story 3 - List all items
def sailorscouts_list(request):
    sailors = Scout.Scouts.all()
    content = {'sailors': sailors}
    return render(request, 'SailorScouts/SailorScouts_list.html',content)

# Story 4 - Details
def sailorscouts_detail(request, pk):
    pk = int(pk)
    sailors = Scout.Scouts.get(pk=pk)
    content = {'sailors': sailors }
    return render(request, 'SailorScouts/SailorScouts_detail.html', content)

# Story 5 - Edit and Delete functions
def sailorscouts_edit(request, pk):
    sailors = get_object_or_404(Scout, id=pk)
    form = ScoutForm(data=request.POST or None, instance=sailors)
    if request.method == 'POST':
        if form.is_valid():
            sailors.save()
            return redirect('sailorscouts_detail', sailors.id)
    content = {'form': form, 'sailors': sailors}
    return render(request, 'SailorScouts/SailorScouts_edit.html', content)

def sailorscouts_delete(request, pk):
    sailors = get_object_or_404(Scout, id=pk)
    if request.method == 'POST':
            sailors.delete()
            return redirect('sailorscouts_list')
    content = {'sailors': sailors}
    return render(request, 'SailorScouts/SailorScouts_delete.html', content)










