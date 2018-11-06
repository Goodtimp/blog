# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from . import models

 #通过分类id得到分类  id空获得所有
@require_http_methods(["GET"])
def GetCategoryById(request):
    response = {}
    try:
        id=request.GET.get("id")
        if id == 0 or id=="0":
            category=models.Category.objects.all()
        else:
            category=models.Category.objects.filter(Id=int(id))
 
        response['category']=json.loads(serializers.serialize("json",category))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

 
 #通过分类id得到相同文章概略 id空获得所有
@require_http_methods(["GET"])
def GetSameArticleByCId(request):
    response = {}
    try:
        id=request.GET.get("id")
        if id == 0 or id=="0":
            Articles=models.Article.objects.all()
        else:
            Articles=models.Article.objects.filter(CategoryId=int(id))
        response['Articles']=json.loads(serializers.serialize("json",Articles))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

 #通过文章id得到文章概略 id空获得所有
@require_http_methods(["GET"])
def GetArticleById(request):
    response = {}
    try:
        id=request.GET.get("id")
        if id == 0 or id=="0":
            Article=models.Article.objects.all()
        else:
            Article=models.Article.objects.filter(Id=int(id))
        response['Article']=json.loads(serializers.serialize("json",Article))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


 #通过文章id得到文章内容 
@require_http_methods(["GET"])
def GetArticleContentById(request):
    response = {}
    try:
        id=request.GET.get("id")
        Content=models.AritcleDatils.objects.filter(ArticleId_id=int(id))
        Article=models.Article.objects.filter(Id=int(id))
        Content=json.loads(serializers.serialize("json",Content))
        Article=json.loads(serializers.serialize("json",Article))
        response['Article']=Article
        response['Content']=Content
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

