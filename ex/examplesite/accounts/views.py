from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Account

# Create your views here.

def index(request):
    school1 = "William G. Enloe High School"
    school2 = "Raleigh Charter High School"
    # account_list = Account.objects.get(school=school2)
    account_list = Account.objects.order_by("last_name")
    output = ', '.join([a.first_name + " " + a.last_name for a in account_list])
    '''
    template = loader.get_template('accounts/index.html')
    context = {
        'account_list': account_list
    }
    return render(request, 'accounts/index.html', context)
    '''
    return HttpResponse(output)
