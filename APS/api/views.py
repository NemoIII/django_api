from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import PostUpdate

def update_model_detail_view(request):
    data = {
        "count": 1000,
        "content": "New content"
    }
    return JsonResponse(data)
