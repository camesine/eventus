from __future__ import unicode_literals

from django.shortcuts import render
from .models import Event, Category

def index(request):
    events = Event.objects.all().order_by('-created')[:6]
    categories = Category.objects.all()
    print events
    print categories
    return render(request, 'index.html', {
        'events': events,
        'categories': categories
    })
