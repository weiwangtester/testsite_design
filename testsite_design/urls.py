"""
URL configuration for testsite_design project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.views.generic.base import RedirectView

urlpatterns = [
    # grappelli URLs should be placed before the admin URLs
    path('grappelli/', include('grappelli.urls')),
    path('', RedirectView.as_view(url='/admin/')),
    path('admin/', admin.site.urls),
    # 公共app路由分发到公共app的urls
    path('common_app/', include('common_app.urls')),
    # 销售云的路由分发到销售云的urls
    path('project_b/', include('project_b.urls')),
    # 商业云的路由分发到商业云的urls
    path('project_a/', include('project_a.urls')),
]
