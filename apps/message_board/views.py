from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def index(request):
    return render(request, "message_board/index.html")


def register(request):
    error = False
    if len(request.POST['first_name']) < 2:
        error = True
        messages.error(
            request, "First name must be a minimum length of three characters!")

    if request.POST['first_name'].isalpha() == False:
        error = True
        messages.error(
            request, "First name cannot have a number in it or be blank!")

    if len(request.POST['last_name']) < 2:
        error = True
        messages.error(
            request, "Last name must be a minimum of three characters!")

    if request.POST['last_name'].isalpha() == False:
        error = True
        messages.error(
            request, "Last name cannot have a number in it or be blank!")

    if len(request.POST['email']) < 7:
        error = True
        messages.error(
            request, "Email must be a minimum length of seven characters!")

    if not EMAIL_REGEX.match(request.POST['email']):
        error = True
        messages.error(
            request, "Email must be a valid email address!")

    if len(request.POST['password']) < 8:
        error = True
        messages.error(
            request, "Password must be a minimum length of eight characters!")

    if request.POST['password'] != request.POST['confirm_password']:
        error = True
        messages.error(
            request, "Passowrds must match!")

    if User.objects.filter(email=request.POST['email']):
        error = True
        messages.error(
            request, "User already exists!")

    if error:
        return redirect('/')

    hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    decoded_hash = hashed.decode('utf-8')

    user = User.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=decoded_hash)
    print(user)
    request.session['u_id'] = user.id
    return redirect('/board')


def login(request):
    pass


def board(request):
    context = {
        'posts': Message.objects.all()
    }
    return render(request, "message_board/board.html", context)


def post(request):
    pass


def comment(request):
    pass


def deleteMessage(request):
    pass


def deleteComment(request):
    pass


def logout(request):
    pass
