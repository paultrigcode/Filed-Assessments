"""audio_file_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import re_path, include
from crudapi.views.api.crud import ArticleView,ArticleDetail


# from crudapi.views import api
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# router = DefaultRouter()
# router.register(r'audiofile', api.ApiViewSet,basename='audiofile')
# router.register(r'song/<int:pk>/', api.DeleteViewSet,basename='audio')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # re_path(r'^api/', include(router.urls)),
    path('create/', ArticleView.as_view()),
    path('<slug:slug>/<int:pk>', ArticleView.as_view()),
    path('<slug:slug>/', ArticleView.as_view()),
    path('asd/<slug:slug>/<int:pk>', ArticleDetail.as_view())




]


