from django.conf.urls import url, include
from . import views



urlpatterns = [url(r"acid$",views.GetSameArticleByCId),url(r'cid$', views.GetCategoryById),
url(r"aid$",views.GetArticleById),url("id$",views.GetArticleContentById)]