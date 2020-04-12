from django.http import JsonResponse
from django.shortcuts import render

# from third party imports
from rest_framework.response import Response
from rest_framework.views import APIView


class test_view(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'Ishwor',
            'age': 23,
        }
        return Response(data)

# def test_view(request):
#     data = {
#         'name': 'Ishwor',
#         'age': 23,
#     }
#     return JsonResponse(data)
