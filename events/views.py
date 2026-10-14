
from django.shortcuts import render, get_object_or_404
from .models import Event,Registration
def home(request):
    return render (request, 'events/home.html')

def event_list(request):
    events= Event.objects.all()
    return render(request, 'events/event_list.html',{
        'events': events
    })

def event_detail(request,id):
    event = get_object_or_404(Event, id=id)

    return render(request, 'events/event_detail.html', {
        'event': event
    })

    
def register(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_email = request.POST.get('student_email')
        event_id = request.POST.get('event_id')

        event = get_object_or_404(Event, id=event_id)

        Registration.objects.create(
            event=event,
            student_name=student_name,
            student_email=student_email
        )

        return render(request, 'events/register.html', {
            'message': 'Registration successful!'
        })

    return render(request, 'events/register.html')

    