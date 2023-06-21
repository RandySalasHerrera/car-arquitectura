"""app_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include,path
from django.views.generic import RedirectView
from base.api import views
from coursescraped import views as views_coursescraped
from course.api.router import router_course
from qualification.api.router import router_qualification
from student.api.router import router_student
from teacher.api.router import router_teacher

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", RedirectView.as_view(url="admin/")),
    path("", views_coursescraped.index),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", include("coursescraped.api.urls")),
    path("", include("base.api.urls")),

    path('api/v1/', include(router_course.urls)),
    path('api/v1/', include(router_qualification.urls)),
    path('api/v1/', include(router_student.urls)),
    path('api/v1/', include(router_teacher.urls)),
]
 