# ------ 13
# En este archivo definiremos nuestras rutas

from django.urls import path

# ------ 14
# Importamos Nuestras vistas

from .views import Index, Blog_list, Blog_Detail

urlpatterns = [
    path('', Index),
    path('blog/', Blog_list),
    path('<int:pk>/', Blog_Detail, name='detailpost'),
]
