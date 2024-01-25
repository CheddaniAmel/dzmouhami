from django.http.response import JsonResponse
from django.contrib.auth import authenticate, login, logout
from .models import ProfilAvocat , Avis
from .serializers import ProfilAvocatSerializer ,ClientSignUpSerializer,AvisSerializer,BlogSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from geopy.geocoders import Nominatim
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView


class ProfilAvocatDetailView(generics.RetrieveAPIView):
    queryset = ProfilAvocat.objects.all()
    serializer_class = ProfilAvocatSerializer




class ProfilAvocatBlogsView(generics.RetrieveAPIView):
    queryset = ProfilAvocat.objects.all()
    serializer_class = BlogSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        blogs = instance.blogs.all()
        serializer = self.get_serializer(blogs, many=True)
        return Response(serializer.data)

    


@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, username=email, password=password)

    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key, 'user': user.email})
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=400)
  





@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_avis_to_profilavocat(request, profilavocat_id):
    try:
        profil_avocat = ProfilAvocat.objects.get(id=profilavocat_id)
        print(profil_avocat.avocat.nom)
    except ProfilAvocat.DoesNotExist:
        print("profil_avocat not found ")
        return Response({"error": "ProfilAvocat not found"}, status=status.HTTP_404_NOT_FOUND)
        

    if request.method == 'POST':
        serializer_data = request.data.copy()
        
        # Associate the review with the currently authenticated user
        serializer_data['client'] = request.user.id
        
        serializer = AvisSerializer(data=serializer_data)
        
        if serializer.is_valid():
            # Check if the client has already provided a review for this lawyer
            existing_avis = Avis.objects.filter(client=request.user, avocat=profil_avocat.avocat)
            if existing_avis.exists():
                return Response({"error": "You have already provided a review for this lawyer"}, status=status.HTTP_400_BAD_REQUEST)

            # Save the new review
            serializer.save(avocat=profil_avocat.avocat)

            # You might want to update the overall rating of the lawyer's profile based on this new review.
            # You can implement this logic in your models or serializers.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def Trusted_lawyers(request):
    avocat = ProfilAvocat.objects.order_by('-rating')[:3]
    serializer = ProfilAvocatSerializer(avocat, many =True) 
    return Response(serializer.data)


@api_view(['GET'])
def get_highest_rated_avis(request):
    # Get the Avis with the highest rating
    highest_rated_avis = Avis.objects.order_by('-rating').first()
    serializer = AvisSerializer(highest_rated_avis) 
    return Response(serializer.data)



@api_view(['POST'])
def signup(request):
    serializer = ClientSignUpSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, 
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
   
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'})



#start funct filtering
class ProfilAvocatFilter(django_filters.FilterSet):
    specialisation__name = django_filters.CharFilter(field_name='avocat__specialisation__name', lookup_expr='icontains')
    langue__name = django_filters.CharFilter(field_name='avocat__langue__name', lookup_expr='icontains')
    rating = django_filters.NumberFilter(field_name='rating', lookup_expr='exact')
    adresse = django_filters.CharFilter(field_name='avocat__adresse', lookup_expr='icontains')


    class Meta:
        model = ProfilAvocat
        fields = ['specialisation__name', 'langue__name', 'rating']

class ProfilAvocatListView(ListAPIView): 
    serializer_class = ProfilAvocatSerializer
    filterset_class = ProfilAvocatFilter
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        queryset = ProfilAvocat.objects.all()
        entered_adresse = self.request.query_params.get('adresse', '')
        print("entered_adresse:", entered_adresse)

        # Filter the queryset based on the entered_adresse
        queryset = queryset.filter(avocat__adresse__icontains=entered_adresse)
        return queryset
#finish filtering
    

