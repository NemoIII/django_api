import json
from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import PostUpdate
from APS.mixin import JsonRepsponseMixin

def json_example_view(request):
    data = {
        "count": 1000,
        "content": "New content"
    }
    json_data = json.dumps(data)
    # return JsonResponse(data)
    return HttpResponse(json_data, content_type='application/json')


class ApsGet(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "New content"
        }
        return JsonResponse(data)


class ApsGet2(JsonRepsponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "New content"
        }
        return self.render_to_jspn_response(data)