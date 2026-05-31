"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',include('authentication.presentation.urls')),
    path('account/', include('allauth.urls')),   

    path('api/role/', include('features.roles.presentation.api.urls')),
    path('api/rank/', include('features.ranks.presentation.rank_urls')),
    path('api/room/', include('features.rooms.presentation.room_urls')),
    path('api/stype/', include('features.stypes.presentation.stype_urls')),
    path('api/staff/', include('features.staffs.presentation.staff_api')),
    path('api/category/', include('features.categories.urls')),
    path('api/document/', include('features.documents.urls')),
    path('api/building/', include('features.buildings.urls')),
    path('api/log/', include('features.logs.urls')),
    path('api/dtype/', include('features.dtypes.urls')),
    path('api/', include('features.chats.urls')),
    path('api/department/', include('features.departments.presentation.department_api')),
    path('api/dashboard/', include('features.dashboard.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
