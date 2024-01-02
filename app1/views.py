from django.http.response import JsonResponse
from django.contrib.auth import authenticate, login, logout
from .models import ProfilAvocat
from .serializers import ProfilAvocatSerializer ,ClientSignUpSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from geopy.geocoders import Nominatim

import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView


@api_view(['GET'])
def Trusted_lawyers(request):
    avocat = ProfilAvocat.objects.order_by('-rating')[:3]
    serializer = ProfilAvocatSerializer(avocat, many =True) 
    return Response(serializer.data)


@api_view(['POST'])
def signup(request):
    serializer = ClientSignUpSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    """
    User login view using email and password.
    """
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key, 'user': user.email})
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=400)
    
   
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'})




class ProfilAvocatFilter(django_filters.FilterSet):
    specialisation__name = django_filters.CharFilter(field_name='avocat__specialisation__name', lookup_expr='icontains')
    langue__name = django_filters.CharFilter(field_name='avocat__langue__name', lookup_expr='icontains')
    rating = django_filters.NumberFilter(field_name='rating', lookup_expr='exact')
    adresse = django_filters.CharFilter(field_name='avocat__adresse', lookup_expr='icontains')


    class Meta:
        model = ProfilAvocat
        fields = ['specialisation__name', 'langue__name', 'rating','adresse']



class ProfilAvocatListView(ListAPIView):
    serializer_class = ProfilAvocatSerializer
    filterset_class = ProfilAvocatFilter
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        queryset = ProfilAvocat.objects.all()
        google_maps_link = self.request.query_params.get('adresse', None)
        geolocator = Nominatim(user_agent = "city_extractor")
        try :
            location = geolocator.geocode(google_maps_link, language='en')
            if location and location.address:
                city = location.raw.get('address', {}).get('city')  # Extract city from address
                if city:
                    queryset = queryset.filter(avocat__adresse__icontains=city)
                else:
                    return  ProfilAvocat.objects.none() 

            else:
                return ProfilAvocat.objects.none() 
        except Exception as e:
            return ProfilAvocat.objects.none() 
        return queryset

        
    


