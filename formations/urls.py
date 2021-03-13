from django.urls import path
from .views import WingsGenericAPIView, SquadsGenericAPIView

urlpatterns = [
    path('wings', WingsGenericAPIView.as_view()),
    path('wings/<str:pk>', WingsGenericAPIView.as_view()),
    path('squads', SquadsGenericAPIView.as_view()),
    path('squads/<str:pk>', SquadsGenericAPIView.as_view()),
]