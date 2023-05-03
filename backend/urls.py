from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as viewsSYS
from . import views
from core.views import ListViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'lists', ListViewSet, basename='list')
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth', viewsSYS.obtain_auth_token, name="api-token-auth"),
    path('admin/', admin.site.urls),
]