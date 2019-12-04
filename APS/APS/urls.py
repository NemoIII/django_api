from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from api.views import update_model_detail_view


urlpatterns = [
    url('^$', update_model_detail_view),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
