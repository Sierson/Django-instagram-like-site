from django import views
from django.http import HttpResponseRedirect
from django.urls import reverse

def redirect(request):
    return HttpResponseRedirect(reverse('account:login'))
