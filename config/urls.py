
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from mainapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', ExampleApiView.as_view()),
    path('home/', IndexView.as_view(), name='main'),
    path('<int:pk>', InfoExample.as_view(), name='detail'),
    path('api/<int:pk>', UpdateAPIView.as_view(), name='update'),
    path('api/del/<int:pk>/', DeleteView.as_view()),
    path('api/all/<int:pk>/', AllExample.as_view()),
    path('del/<int:pk>', DeleteView.as_view(), name='delete'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/get/<int:pk>/', GetOnly.as_view(), name='get_only'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
