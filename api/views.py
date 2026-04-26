from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, ArtistSerializer, EventSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Artist, Event


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Usuari registrat correctament"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"error": "Credencials incorrectes"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # Generar JWT
        # `access`: token de curta durada (5 min) per autenticar peticions
        # `refresh`: token de llarga durada (24 h) per obtenir nous tokens access quan caduquin
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )


class EventListView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


class EventDetailView(APIView):
    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(
                {"error": "L'esdeveniment no existeix"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = EventSerializer(event)
        return Response(serializer.data)

class CreateArtistView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateEventView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WelcomeView(APIView):
    def get(self, request):
        return Response({
            "name": "Vertex API",
            "description": "API per gestionar esdeveniments artístics femenins",
            "version": "1.0.0",
            "endpoints": {
                "register": "/api/register/ (POST)",
                "login": "/api/login/ (POST)",
                "events": "/api/events/ (GET)",
                "event-detail": "/api/events/<id>/ (GET)",
                "create_artist": "/api/artists/ (POST)",
                "create_event": "/api/events/create/ (POST)",
            }
        })