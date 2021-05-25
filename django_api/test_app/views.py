from django.shortcuts import render
from django.http import JsonResponse, response
from rest_framework.views import APIView
from django.forms.models import model_to_dict

from .serializers import SimpleSerializer
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

class Simple(APIView):

    def post(self, request):
        serializer = SimpleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # new_ = TestModel.objects.create(
        #     name=request.data["name"],
        #     description=request.data["description"],
        #     phone_number=request.data["phone_number"],
        #     is_live=request.data["is_live"],
        #     amount=request.data["amount"],
        # )
        # return JsonResponse({"data": SimpleSerializer(new_).data})
        # return JsonResponse({"data": model_to_dict(new_)})
        return JsonResponse({"data": serializer.data})

    def get(self, request):
        content = TestModel.objects.all().values()
        return JsonResponse({"data": SimpleSerializer(content, many=True).data})
        # return JsonResponse({"data": list(content)})

    def put(self, request, *args, **kwargs):
        model_id = kwargs.get("id", None)
        if not model_id:
            return JsonResponse({"error": "error"})
        try:
            instance = TestModel.objects.get(id=model_id)
        except:
            return JsonResponse({"error": "error"})
        serializer = SimpleSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"data": serializer.data})
