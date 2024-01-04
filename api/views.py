from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer
from .utils import create_checkout_session
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.status import HTTP_200_OK

class BuyItemView(APIView):
   def get(self, request, id):
       item = get_object_or_404(Item, id=id)
       session_id = create_checkout_session(item)
       return Response({'session_id': session_id}, status=HTTP_200_OK)

class ItemView(APIView):
   def get(self, request, id):
       item = get_object_or_404(Item, id=id)
       serializer = ItemSerializer(item)
       return Response(serializer.data, status=HTTP_200_OK)

            

class MyTokenObtainPairView(TokenObtainPairView):
   serializer_class = MyTokenObtainPairSerializer

class MyTokenRefreshView(TokenRefreshView):
   serializer_class = MyTokenRefreshSerializer