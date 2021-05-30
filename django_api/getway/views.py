from datetime import datetime, timedelta
import random
import string
from rest_framework.views import APIView

from django.shortcuts import render

# Create your views here.
import jwt
from .models import Jwt
from user.models import CustomUser
from .serializers import LoginSerializer
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.response import Response


def get_random(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def get_access_token(payload):
    return jwt.encode(
        {"exp": datetime.now() + timedelta(minutes=5), **payload},
        settings.SECRET_KEY, algorithm="HS256"
    )

def get_refresh_token():
    return jwt.encode(
        {"exp": datetime.now() + timedelta(days=365), "data": get_random(10)},
        settings.SECRET_KEY, algorithm="HS256"
    )


class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        if not user:
            return Response({"error": "error"}, status="400")

        access = get_access_token({
            "user_id": user.id
        })
        refresh = get_refresh_token()

        Jwt.objects.create(
            user_id=user.id,
            access=access,
            refresh=refresh
        )
        return Response({"access": access, "refresh": refresh})