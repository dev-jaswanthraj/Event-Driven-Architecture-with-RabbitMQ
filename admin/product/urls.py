from django.urls import path
from .views import ProductViewSet, UserAPIView

urlpatterns = [
    path('product', ProductViewSet.as_view({
        'get':'list',
        'post': 'create',
    })),
    path('product/<str:pk>', ProductViewSet.as_view({
        'get':'retrieve',
        'delete': 'destroy',
        'put': 'update'
    })),
    path('user', UserAPIView.as_view()),
]