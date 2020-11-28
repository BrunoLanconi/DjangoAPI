from django.contrib import admin
from django.urls import path, include
from freshot.views import StudentsViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'students', StudentsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
