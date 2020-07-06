from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import UpdateView, DetailView
from django.views.generic.edit import DeleteView
from .forms import AddProductForm
from django.urls import reverse_lazy

def products_list(request):
    contexts = {
        'products': Product.objects.all().order_by('-created_at')[:10]
    }
    return render(request, 'products/products_list.html', contexts)

def add_product(request):
    if request.method == 'POST':
        add_form = AddProductForm(request.POST, request.FILES)
        if add_form.is_valid():
            add_form.save()
            return redirect('products_list')

    else: add_form = AddProductForm()
    return render(request, 'products/add_product.html', {'add_form': add_form})

class ItemUpdateView(UpdateView):
    model = Product
    fields = ['name','description', 'price', 'brand', 'picture']
    template_name = 'products/update_product.html'

class ItemDetailView(DetailView):
    model = Product


class ItemDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products_list')