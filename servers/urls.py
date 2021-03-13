from django.urls import path
from .views import ServerGenericAPIView, ExportServerAPIView

urlpatterns = [
    path('servers', ServerGenericAPIView.as_view()),
    path('export-server', ExportServerAPIView.as_view())
]