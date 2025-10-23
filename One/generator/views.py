import string

from django.shortcuts import render
# from django.http import HttpResponse
import random


def home(request):
    lst = list(range(6, 15))
    return render(request, 'generator/home.html', {"lst": lst})


def password(request):
    chars = [chr(i) for i in range(97, 123)]

    if request.GET.get('uppercase'):
        chars.extend([chr(i) for i in range(65, 91)])

    if request.GET.get('numbers'):
        chars.extend([chr(i) for i in range(48, 58)])

    if request.GET.get('symbol'):
        symbols = string.punctuation
        chars.extend(symbols)

    psw = ""
    length = int(request.GET.get('length'))
    for i in range(length):
        psw += random.choice(chars)
    return render(request, "generator/password.html", {"psw": psw})


def rules(request):
    return render(request, "generator/rules.html")