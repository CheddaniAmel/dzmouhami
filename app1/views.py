from django.http.response import JsonResponse
from .models import ProfilAvocat
from rest_framework.decorators import api_view
from .serializers import ProfilAvocatSerializer
from rest_framework.response import Response

@api_view(['GET'])
def Trusted_lawyers(request):
    avocat = ProfilAvocat.objects.order_by('-rating')[:3]
    serializer = ProfilAvocatSerializer(avocat, many =True) 
    return Response(serializer.data)

