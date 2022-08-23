from django.urls import path, include
from .views import get_name, home
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.conf.urls.static import static

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
	path('sample', get_name),
    path('<pk>', home),
    path('', home),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)