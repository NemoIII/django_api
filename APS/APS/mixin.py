from django.http import JsonResponse

class JsonRepsponseMixin(object):
    def render_to_jspn_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)
    
    def get_data(self, context):
        return context

