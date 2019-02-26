# -*- coding: utf-8 -*-
"""backsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

# this is xadmin
import xadmin

xadmin.autodiscover()
from xadmin.plugins import xversion

xversion.register_models()
# this is xadmin

# this is markdown
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
# end

# this is 富文本编辑器
# from django.conf.urls.static import static
# import DjangoUeditor.urls
# import os
# end

from django.conf import settings
from blog import views as api
urlpatterns = [
    url(r"^xadmin/", xadmin.site.urls),
    # url(r'', xadmin.site.urls),
    # url(r"^ueditor/", include(DjangoUeditor.urls)),
    url(r'mdeditor/', include('mdeditor.urls')),
    url(r"^api/", include(blog.urls)),
    url(r"", TemplateView.as_view(template_name="index.html")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    