from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout

from .models import Invoice


class Login(View):
    def post(self, request):
        if request.user.is_anonymous:
            name = request.POST.get('name')
            password = request.POST.get('password')
            user = authenticate(username=name,
                                password=password)
            if user:
                login(request, user)
                return redirect('/invoices')
            else:
                template = "login.html"
                title = "Авторизация"
                return render(request, template, {'title': title, 'error': True})

        else:
            return redirect('/invoices')

    def get(self, request):
        if request.user.is_anonymous:
            template = "login.html"
            title = "Авторизация"
            return render(request, template, {'title': title})
        else:
            return redirect('/invoices')


@login_required
def logout(request):
    django_logout(request)
    return redirect('/login')


@login_required
def invoices(request):
    template = "invoices.html"
    invoices = Invoice.objects.all()
    title = "Список накладных"
    return render(request, template, {'invoices': invoices,
                                      'title': title})





class InvoiceDetail(View):
    def post(self, request, invoice_id):
        if request.user.is_anonymous:
            redirect('/login')
        invoice = Invoice.objects.filter(pk=invoice_id).first()
        if invoice:
            invoice.full_text = request.POST.get('full_text')
            invoice.text = request.POST.get('text')
            invoice.save()
        return redirect(request.path)

    def get(self, request, invoice_id):
        if request.user.is_anonymous:
            return redirect('/login')
        template = 'invoice_detail.html'
        invoice = Invoice.objects.filter(pk=invoice_id).first()
        title = invoice.name if invoice else 'Данный продукт не найден'
        return render(request, template, {'invoice': invoice,
                                          'title': title})

@login_required
def redirect_to_invoices(request):
    return redirect('/invoices')