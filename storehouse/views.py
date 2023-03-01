from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import *
from .forms import *
# Create your views here.

def stores(request):
    store=Store.objects.all()
    return render(request,'stores/stores.html',{
        'store':store,
        'title':Store.objects.all(),
    })

def add_new_store(request):
    form=StoreForm()
    if request.method=='POST':
        form=StoreForm(request.POST)
        if form.is_valid:
            store=form.save()
            return redirect('stores')
    
    return render(request,'stores/add_store.html',{
        'form':form
    })

def delete_store(request,slug):
    store=Store.objects.get(slug=slug)
    store.delete()
    return redirect('stores')


def store_details(request,slug):
    category=Category.objects.filter(store__slug=slug).all()
    store=Store.objects.get(slug=slug)
    return render(request,'stores/store_details.html',{
        'category':category,
        'store':store
    })

def add_details(request,slug):
    store=Store.objects.get(slug=slug)
    if request.method == 'POST':
        form=DetailsForm(request.POST)
        if form.is_valid:
            category=form.save(commit=False)
            category.store=store
            category.save()
            return redirect('store_details', slug=store.slug)
    form=DetailsForm()
    return render(request,'stores/add_details.html',{
        'form':form,
        'store':store,
    })

def delete_details(request,slug,id):
    store=Store.objects.get(slug=slug)
    category=Category.objects.get(pk=id)
    category.delete()
    return redirect('store_details', slug=store.slug)

class DetailsUpdateView(UpdateView):
    model = Category
    fields=['name','count']
    template_name = "stores/update_details.html"
    context_object_name='category'
    pk_url_kwarg='id'
    success_url=reverse_lazy('stores')



