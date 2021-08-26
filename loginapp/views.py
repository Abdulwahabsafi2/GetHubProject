from django.shortcuts import render
from django.http import HttpResponse

from .forms import LoginForm


def login_view(request):
    template = "loginapp/login.html"
    form = LoginForm()

    context = {
        "form": form,
    }
    return render(request, template, context)
