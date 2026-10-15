
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event,Registration
from django.contrib.auth import authenticate, login

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

    
def event_create(request):
    if request.method == 'POST':
        Event.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            date=request.POST.get('date'),
            time=request.POST.get('time'),
            location=request.POST.get('location'),
            capacity=request.POST.get('capacity'),
            organizer=request.POST.get('organizer'),
        )

        return redirect('event_list')

    return render(request, 'events/event_form.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            return render(request, 'events/login.html', {
                'error': 'Invalid username or password.'
            })

    return render(request, 'events/login.html')
    return render(request, 'events/login.html')

def event_confirm_delete(request, id):
    event = get_object_or_404(Event, id=id)

    if request.method == 'POST':
        event.delete()
        return redirect('event_list')

    return render(request, 'events/event_confirm_delete.html', {
        'event': event
    })