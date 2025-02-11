from django.urls import path
from .views import (CategoryListView,CategoryDetailView,ProductListView,ProductDetailView,
                    FileListView,FileDetailView)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = [
    path('category/',CategoryListView.as_view()),
    path('category/<int:pk>/',CategoryDetailView.as_view()),
    path('product/',ProductListView.as_view()),
    path('product/<int:pk>/',ProductDetailView.as_view()),
    path('file/',FileListView.as_view()),
    path('file/<int:pk>/',FileDetailView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]