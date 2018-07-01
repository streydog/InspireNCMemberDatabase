from django.http import HttpResponse
from django.shortcuts import render

from .models import Account

def account_list(request):
    accounts = Account.objects.all().order_by('last_name')
    return render(request, 'accounts/account_list.html', {'accounts': accounts})

def account_detail(request, slug):
    # return HttpResponse(slug)
    account = Account.objects.get(slug=slug)
    return render(request, 'accounts/account_detail.html', {'account': account})

def signup_view(request):
    return render(request, 'accounts/account_signup.html')
