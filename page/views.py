from django.shortcuts import render
from .models import Event
from django.utils import timezone

def homepage(request):
    latest = Event.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0]
    last_but_one = Event.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[1]
    return render(request, 'page/homepage.html', {'latest':latest, 'last_but_one':last_but_one})

def events(request):
    events = Event.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'page/events.html', {'events':events})

def program(request):
    return render(request, 'page/program.html', {})

def signup(request):
    return render(request, 'page/signup.html', {})
