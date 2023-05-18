from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .users.views import UserViewSet, UserCreateViewSet
from api.users.views import PublicationViewSet, FollowViewSet, SocialUserViewSet

router = DefaultRouter()                        # Creas el objeto de configuracion a rutas.
router.register(r'users', UserViewSet)          # Registras nuevas rutas.
router.register(r'users', UserCreateViewSet)
router.register(r'publications', PublicationViewSet)
router.register(r'follows', FollowViewSet)
router.register(r'social-users', SocialUserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),      # incluye las rutas
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
