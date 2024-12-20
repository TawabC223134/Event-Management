from django.urls import path
from .views import EventListView, EventCreateView, EventUpdateView, EventDeleteView, RegisterView, UserLoginView

urlpatterns = [
    path('list/', EventListView.as_view(), name='event_list'),
    path('create/', EventCreateView.as_view(), name='event_create'),
    path('update/', EventUpdateView.as_view(), name='event_update'),
    path('delete/', EventDeleteView.as_view(), name='event_delete'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]
