import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from forms import UserForm, LoginForm
from . import database
from .models import *
options = {'login': LoginForm(), 'form': UserForm()}
# Create your views here.
def index(request):
    return render(request, 'myindex.html', options)

def mtrivia(request):
    return render(request, 'mtrivia.html', options)

def new_user(request, error=None):
    if error:
        error = int(error)
        if error == 0:
            options['confirm'] = True
        elif error == 1:
            options['error'] = 'That username already exists.'
        elif error == 2:
            options['error'] = 'Form was invalid.'
    return render(request, 'new_user.html', options)

def create_user(request):
    if request.method == 'POST':
        print request.POST['username']
        form = UserForm(request.POST)
        valid = form.is_valid()
        if valid:
            form = form.cleaned_data
            if User.objects.filter(username=form['username']).exists():
                return redirect('/newuser/1/')
            else:
                user = User.objects.create_user(username=form['username'], email=form['email'], password=form['password'])
                user.first_name = form['first_name']
                user.last_name = form['last_name']
                user.save()
                request.session['user'] = user
                return redirect('/newuser/0/')
        return redirect('/newuser/2/')
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form = form.cleaned_data
        user = authenticate(username=form.username, password=form.password)
        if(user is None):
            #Redirect and error#
            return redirect('/')
        else:
            request.session['user'] = user
            return redirect('/')
def logout(request):
    request.session['user'].pop()
    return redirect(request.url)

def openshift(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())
def update_leaderboard(request, score):
    if request.method == 'POST' and 'user' in request.session:
        Scores.objects.create(user=request.session['user'], score=score).save()

def leaderboard(request):
    board = Scores.objects.order_by('score')[:10]
    options['board'] = board
    return render(request, 'leaderboard.html', options)

def calculator(request):
    return render(request, 'calculator.html', options)