from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Vakanсy
from django.contrib.auth import login, authenticate, logout, get_user_model
from .forms import NewUserForm, PostForm
from django.contrib.auth.forms import AuthenticationForm
import requests
from django.contrib.auth.decorators import login_required

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

def teendescription(request):
    return render(request, "./TeenDescryption.html")

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
