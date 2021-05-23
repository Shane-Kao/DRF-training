from django.shortcuts import render
from django.http import JsonResponse, response
from rest_framework.views import APIView
from django.forms.models import model_to_dict

from .models import TestModel
# Create your views here.


# def simple(request):
#     # return response.HttpResponse("Welcome")
#     method = request.method.lower()
#     if method == 'get':
#         return JsonResponse({"data": request.method})
#     elif method == "post":
#         return JsonResponse({"data": "Add data"})
#     elif method == "put":
#         return JsonResponse({"data": "Update data"})
#     return JsonResponse({"error": "method not allowed"})

class simple(APIView):
    def post(self, request):
        new_ = TestModel.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            phone_number=request.data["phone_number"],
            is_live=request.data["is_live"],
            amount=request.data["amount"],
        )
        return JsonResponse({"data": model_to_dict(new_)})

    def get(self, request):
        content = TestModel.objects.all().values()
        return JsonResponse({"data": list(content)})