"""backsite URL Configuration

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
from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
import blog.urls

from django.conf import settings
from DjangoUeditor import urls as djud_urls
from blog import views as api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/',include(djud_urls)),
    url(r'^api/',include(blog.urls)),
    url(r'',TemplateView.as_view(template_name="index.html")),
]
'''
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns =urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
'''