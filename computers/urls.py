from django.urls import path
from .views import ComputerGenericAPIView, CPUGenericAPIView, RAMGenericAPIView, MonitorGenericAPIView, OSGenericAPIView, BrandGenericAPIView, ExportAPIView

urlpatterns = [
    path('computers', ComputerGenericAPIView.as_view()),
    path('cpus', CPUGenericAPIView.as_view()),
    path('rams', RAMGenericAPIView.as_view()),
    path('monitors', MonitorGenericAPIView.as_view()),
    path('oss', OSGenericAPIView.as_view()),
    path('brands', BrandGenericAPIView.as_view()),
    path('computers/<str:pk>', ComputerGenericAPIView.as_view()),
    path('export', ExportAPIView.as_view()),
]