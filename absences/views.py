from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import AddPersonForm,AddDetailsForm
from django.views.generic import UpdateView
from django.urls import reverse_lazy,reverse
# Create your views here.

def person(request):
    persons=Person.objects.all()
    return render(request,'absences/persons.html',{
        'persons':persons
    })

def add_person(request):
    person=Person.objects.all()
    if request.method == 'POST':
        form=AddPersonForm(request.POST)
        if form.is_valid():
            person=form.save()
            return redirect('person')
    form=AddPersonForm()
    return render(request,'absences/add_person.html',{
        'person':person,
        'form':form
    })

def delete_person(request,slug):
    person=Person.objects.get(slug=slug)
    person.delete()
    return redirect('person')

def person_details(request,slug):
    day=Day.objects.filter(person__slug=slug).all()
    person=Person.objects.get(slug=slug)
    return render(request,'absences/person_details.html',{
        'details':person,
        'day':day
    })

def add_details(request,slug):
    person=Person.objects.get(slug=slug)
    if request.method == 'POST':
        form=AddDetailsForm(request.POST)
        if form.is_valid():
            day=form.save(commit=False)
            day.person=person
            day.save()
            return redirect('person_details' ,slug=person.slug)
    form=AddDetailsForm()
    return render(request,'absences/add_details.html',{
        'person':person,
        'form':form
    })

def delete_details(request,slug,id):
    person=Person.objects.get(slug=slug)
    day=Day.objects.get(pk=id)
    day.delete()
    return redirect('person_details' ,slug=person.slug)


def detail_update(request,slug,id):
    day=Day.objects.get(pk=id)
    person=Person.objects.get(slug=slug)
    if request.method == 'POST':
        form=AddDetailsForm(request.POST,instance=day)
        if form.is_valid():
            day=form.save(commit=False)
            day.person=person
            day.save()
            return redirect('person_details',person.slug)
    form=AddDetailsForm(instance=day)
    return render(request,'absences/update_details.html',{
        'form':form,
        'person':person
    })