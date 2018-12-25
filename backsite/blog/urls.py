# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views



urlpatterns = [url(r"acid$",views.GetSameArticleByCId),url(r'cid$', views.GetCategoryById),
url(r"aid$",views.GetArticleById),url("id$",views.GetArticleContentById),url("like",views.AddLikeNum),
url(r"comment$",views.AddComment),
url(r"getallcom$",views.GetCommentsByArticleId),
url(r"upload",views.upload),
url(r"pyrequest",views.pyrequest)]