from django.urls import path
from .views import RegisterView, LoginView, EventListView, EventDetailView, CreateArtistView, CreateEventView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('artists/', CreateArtistView.as_view(), name='create-artist'),
    path('events/create/', CreateEventView.as_view(), name='create-event'),
]