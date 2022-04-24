from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    developers = Developer.objects.all()
    return render(request, 'home.html', {'developers': developers})

def login(request):
    return render(request, 'login.html')

def developer(request, dev_id):
    developer = Developer.objects.get(pk=dev_id)
    projects = Project.objects.filter(id_dev=dev_id)
    return render(request, 'developer.html', {'developer': developer, 'projects':projects})

def project(request, project_id):
    project = Project.objects.get(pk=project_id)
    replies = Reply.objects.filter(id_project=project_id)
    replies = [(reply, Client.objects.get(pk=reply.id_client_id)) for reply in replies]
    #developer = Developer.objects.get(pk=project_id)
    return render(request, 'project.html', {'developer':developer, 'project': project, 'replies':replies})

def new_reply(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.method == 'POST':
        rating = request.POST['rating']
        description = request.POST['description']
        user = Client.objects.first()

        reply = Reply.objects.create(
            rating=rating,
            description=description,
            id_client=user,
            id_project=project
        )

    return render(request, 'new_reply.html', {'project': project})

def devsignup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        firstname = request.POST.get('firstname', False)
        lastname = request.POST.get('lastname', False)
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        street = request.POST.get('street', False)
        zip = request.POST.get('zip', False)
        place = request.POST.get('place', False)
        phone = request.POST.get('phone', False)
        country = request.POST.get('country', False)
        position = request.POST.get('position', False)
        about = request.POST.get('about', False)
        image = request.POST.get('image', False)

        developer = Developer.objects.create(
            firstname = firstname,
            lastname = lastname,
            email =email,
            password = password,
            street = street,
            zip = zip,
            place = place,
            country = country,
            phone = phone,
            position = position,
            about = about,
            image = image,)
    # return redirect('home')

    return render(request, 'devsignup.html')

def clientsignup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname', False)
        lastname = request.POST.get('lastname', False)
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        street = request.POST.get('street', False)
        zip = request.POST.get('zip', False)
        place = request.POST.get('place', False)
        phone = request.POST.get('phone', False)
        country = request.POST.get('country', False)
        about = request.POST.get('about', False)
        image = request.POST.get('image', False)

        client = Client.objects.create(
            firstname = firstname,
            lastname = lastname,
            email =email,
            password = password,
            street = street,
            zip = zip,
            place = place,
            country = country,
            phone = phone,
            about = about,
            image = image,
        )

    return render(request, 'clientsignup.html')
