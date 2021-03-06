# artifacts/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"artifacts", views.ArtifactViewSet, "artifact")

urlpatterns = [
    path("", include(router.urls)),
]
