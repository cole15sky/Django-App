from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse



def homepage(request):
    return HttpResponse("Welcome to the homepage!")



urlpatterns = [
    path('admin/', admin.site.urls),
     path('', homepage, name='home'),  
    path('peep/', include('peep.urls')),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
