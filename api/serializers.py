from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    # write_only=True: La contrasenya només es pot enviar (en el registre),
    # però no es pot llegir (en les respostes de l'API)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        # Mètode create_user de Django: 
        # crea un nou usuari i encripta la contrasenya automàticament
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user