
from django.urls import path,include

from app_coder.views import curso

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>/', curso),
    path('/App-coder/', include('app_coder.urls')),
]
