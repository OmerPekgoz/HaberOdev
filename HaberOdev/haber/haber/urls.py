"""
URL configuration for haber project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from videolar import views

from django.conf.urls.static import static
from django.conf import settings
import streamlit as st
st.write(st.__version__)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="Ana Sayfa"),
    path('haber/<int:sonhaber_id>',views.sonhaberdetay,name="sonhaberdetay"),
    path('gün/<int:gün_id>',views.sonhaberdetay,name="gündemdetay"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)