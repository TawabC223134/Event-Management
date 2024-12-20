from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Event

#Log in
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

# User Registration View (Class-Based)
class RegisterView(CreateView):
    model = Event
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('event_list')

    def form_valid(self, form):
        # Automatically log in the user after successful registration
        response = super().form_valid(form)
        login(self.request, form.save())
        return response

# User Login View (Class-Based)
class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('event_list')

#Event List 
class EventListView(ListView):
    model = Event
    template_name = 'event/event_list.html'
    context_object_name = 'event'

class EventCreateView(CreateView):
    model = Event
    template_name = 'event/event_form.html'
    fields = ['title', 'description', 'location', 'date_time', 'capacity', 'status']
    success_url = reverse_lazy('event_list')

class EventUpdateView(UpdateView):
    model = Event
    template_name = 'events/event_form.html'
    fields = ['title', 'description', 'location', 'date_time', 'capacity', 'status']
    success_url = reverse_lazy('event_list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')