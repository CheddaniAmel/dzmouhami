from rest_framework import serializers
from .models import Avocat, Blog, ProfilAvocat, Client, Avis, RendezVous

from django.contrib.auth import get_user_model

class ClientSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Client
        fields = ['email', 'first_name', 'last_name', 'mobile', 'password']

    def create(self, validated_data):
        user = Client.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            mobile=validated_data['mobile'],
            password=validated_data['password']
        )
        return user 



class AvocatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avocat
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class ProfilAvocatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilAvocat
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class AvisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avis
        fields = '__all__'

class RendezVousSerializer(serializers.ModelSerializer):
    class Meta:
        model = RendezVous
        fields = '__all__'
