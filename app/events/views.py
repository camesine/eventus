from __future__ import unicode_literals

from django.shortcuts import render
from .models import Event, Category

def index(request):
    events = Event.objects.all().order_by('-created')[:6]
    categories = Category.objects.all()

    return render(request, 'events/index.html', {
        'events': events,
        'categories': categories
    })

def main_panel(request):
    events = Event.objects.filter(organizer__username="")
    cantidad = events.count()
    return render(request, 'events/panel/panel.html', { 'events': events, 'cantidad': cantidad })

def crear_evento(request):
    if request.method == 'POST':
        modelform = EventoForm(request.POST, request.FILES)
        if modelform.id_valid():
            organizador = User.objects.get(pk=3)
            nuevo = modelform.save()
            nuevo.organizer = organizador
            nuevo.save()
            return redirect(reverse('events_app: panel'))
        else:
            modelform = Eventform()

        return render(request, 'events/panel/crear_evento.html', { 'form': modelform })

