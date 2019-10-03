import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm


class Login(View):
    def post(self, request):
        pass

    def get(self, request):
        template = "login.html"
        login_form = LoginForm()
        title = "Авторизация"
        return render(request, template, {'login_form': login_form, 'title': title})


@login_required
def logout(request):
    logout(request)
    return redirect('/')


@login_required
def create_invoices(request):
    pass


@login_required
def redirect_to_create_invoices(request):
    pass