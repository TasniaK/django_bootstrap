"""django_bootstrap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# mysite url pattern, adds no prefix to mysite urls (such as index url)
# for admin urls, they get added with the 'admin/ prefix'
# make sure admin url pattern is first as it is more specific regex than mysite url pattern
# static bit makes django return the images etc.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('mysite.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

