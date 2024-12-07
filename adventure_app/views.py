from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Vakanсy
from django.contrib.auth import login, authenticate, logout, get_user_model
from .forms import NewUserForm, PostForm
from django.contrib.auth.forms import AuthenticationForm
import requests
from django.contrib.auth.decorators import login_required
from .forms import ChildRegistrationForm, ParentRegistrationForm, EmployerRegistrationForm

categories = Category.objects.all()
vakancys = Vakanсy.objects.all()

def home_page(request):
    return render(request, "./Registration.html")

def empVacancy(request):
    context = {
        'vakancys': vakancys
    }
    return render(request, './EmployerVacancy.html', context)

def teenTask(request):
    return render(request, "./TeenTask.html")

def teenVacancy(request):
    return render(request, "./TeenVacancy.html")

def emplEdit(request):
    return render(request, "./EmployerEdit.html")

def teendescription(request):
    return render(request, "./TeenDescryption.html")

def teenProf(request):
    return render(request, "./TeenMain.html")

def employProf(request):
    return render(request, "./EmployerMain.html")

def parentProf(request):
    return render(request, "./ParentVIew.html")

def empVacancy(request):
    return render(request, "./EmployerVacancy.html")

def empTeen(request):
    return render(request, "./EmployerTeen.html")

def empMyTeen(request):
    return render(request, "./EmployerTeen.html")

def search_action(request):
    query = request.GET.get('q')
    vacancys = Vakanсy.objects.filter(name__icontains=query)
    context = {
        'query': query,
        'vacancys': vacancys,
        'categories': categories
    }
    return render(request, "./results.html", context)

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()

    context = {
        'form': form
    }
    return redirect(request, '', context)

def delete_post(request, post_id):
    post = get_object_or_404(Vakanсy, id=post_id)
    if request.method == "POST":  
        post.delete()
        return redirect('')  
    context = {
        'post': post
    }
    return render(request, '', context)

def post_list(request):
    posts = Vakanсy.objects.all()

    context = {
        'posts': posts
    }

    return render(request, '', context)

def register_child(request):
    if request.method == "POST":
        form = ChildRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('teenProf')
    else:
        form = ChildRegistrationForm()
    context = {
        'form': form
    }
    return render(request, "./RegistrationTeen.html", context)

def register_parent(request):
    if request.method == 'POST':
        form = ParentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home_page')
    else:
        form = ParentRegistrationForm()
    return render(request, './RegistrationParent.html', {'form': form})

def register_employer(request):
    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home_page')
    else:
        form = EmployerRegistrationForm()
    return render(request, './RegistrationEmploye.html', {'form': form})


