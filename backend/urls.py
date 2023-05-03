from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from . import views
from core.views import ListViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'lists', ListViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]