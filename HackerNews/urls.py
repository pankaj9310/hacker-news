"""HackerNews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from news.views import NewsList, SearchAjaxSubmitView, SearchSubmitView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search-result/',SearchSubmitView.as_view(), name='search-submit'),
    path('search/', SearchAjaxSubmitView.as_view(), name='search-ajax-submit'),
    path('', NewsList.as_view(), name='news_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
