from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import *
from django.views.generic import ListView,View,UpdateView
from django.utils import timezone
from django.views import View as view_based
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required,name='dispatch')
class Home(ListView):
    model=Clients
    template_name='accounts/home.html'
    context_object_name='clients'


class AddClientView(view_based):

    def get(self,request):
        form=AddClient()
        return render(request,'accounts/add_client.html',{
            'form':form
        })
    
    def post(self,request):
        client=Clients.objects.all()
        form=AddClient(request.POST)
        if form.is_valid():
            client=form.save(commit=False)
            client.client=client
            client.created_by=request.user
            client.save()
            return redirect('home')
        return render(request,'accounts/add_client.html',{
            'form':form,
        })





@method_decorator(login_required,name='dispatch')
class ClientDetails(View):

    def get(self, request, slug):
        clients = Clients.objects.get(slug=slug)
        context = {
            "clients": clients,
            #                  related_name
            "category": clients.category.all()
        }
        return render(request,'accounts/client_details.html',context)

def delete_client(request,slug):
    client=Clients.objects.filter(slug=slug)
    client.delete()
    return redirect('home')

# def add_new_category(request,slug):
#     clients=get_object_or_404(Clients,slug=slug)
    
#     if request.method == 'POST':
#         form=AddCategory(request.POST)
#         if form.is_valid():
#             category = form.save(commit=False)
#             category.client=clients
#             category.save()
#             return redirect('client', slug=slug)
#     form=AddCategory()
#     return render(request,'accounts/add_new_category.html',{
#         'form':form,
#         'clients':clients
#     })

class AddNewCategoryView(view_based):

    def get(self,request,slug):
        clients=get_object_or_404(Clients,slug=slug)
        form=AddCategory()
        return render(request,'accounts/add_new_category.html',{
            'form':form,
            'clients':clients
        })
    
    def post(self,request,slug):
        clients=get_object_or_404(Clients,slug=slug)
        form=AddCategory(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.client=clients
            category.created_by=request.user
            category.save()
            return redirect('client', slug=slug)
        return render(request,'accounts/add_new_category.html',{
            'form':form,
            'clients':clients
        })



class CategoryDetailView(view_based):
    def get(self,request,slug,id):
        clients = Clients.objects.get(slug=slug)
        list=List.objects.filter(category__id=id).order_by('-created_dt')
        return render(request,'accounts/category_details.html',{
            'clients':clients,
            'category':Categories.objects.get(client__slug=slug,pk=id),
            'list':list,
        })

def delete_category(request,slug,id):
    client=Clients.objects.filter(slug=slug)
    category=Categories.objects.get(client__slug=slug,pk=id)
    category.delete()
    return redirect('home')

class AddListView(view_based):
    def get(self,request,slug,id):
        category=Categories.objects.all().filter(client__slug=slug)
        form=AddList()
        return render(request,'accounts/add_list.html',{
            'category':Categories.objects.all().filter(client__slug=slug),
            'clients':Clients.objects.get(slug=slug),
            'form':form,
        })
    
    def post(self,request,slug,id):
            clients = Clients.objects.get(slug=slug)
            category=Categories.objects.get(client__slug=slug,pk=id)
            form=AddList(request.POST)
            if form.is_valid():
                list=form.save(commit=False)
                list.category=category
                list.save()
                return redirect('category_details',slug=clients.slug,id=category.pk)
            
            return render(request,'accounts/add_list.html',{
                'category':category,
                'form':form,
                'clients':clients
            })

class ListUpdateView(UpdateView):
    model = List
    fields=['name','count','time','num_motor']
    template_name = "accounts/update_list.html"
    context_object_name='list'
    pk_url_kwarg='list_id'
    def form_valid(self, form):
        list=form.save(commit=False)
        list.updated_dt=timezone.now()
        list.save()
        return redirect('category_details' , slug=list.category.client.slug,id=list.category.pk )



