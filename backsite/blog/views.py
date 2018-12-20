# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from . import models
import random
# this is markdown
import markdown
# 通过分类id得到分类  id空获得所有


@require_http_methods(["GET"])
def GetCategoryById(request):
    response = {}
    try:
        id = request.GET.get("id")
        if id == 0 or id == "0":
            category = models.Category.objects.all()
        else:
            category = models.Category.objects.filter(Id=int(id))

        response['category'] = json.loads(
            serializers.serialize("json", category))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

 # 通过分类id得到相同文章概略 id空获得所有


@require_http_methods(["GET"])
def GetSameArticleByCId(request):
    response = {}
    try:
        id = request.GET.get("id")
        if id == 0 or id == "0":
            Articles = models.Article.objects.all()
        else:
            Articles = models.Article.objects.filter(CategoryId=int(id))
        response['Articles'] = json.loads(
            serializers.serialize("json", Articles))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

 # 通过文章id得到文章概略 id空获得所有


@require_http_methods(["GET"])
def GetArticleById(request):
    response = {}
    try:
        id = request.GET.get("id")
        if id == 0 or id == "0":
            Article = models.Article.objects.all()
        else:
            Article = models.Article.objects.filter(Id=int(id))

        response['Article'] = json.loads(
            serializers.serialize("json", Article))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

 # 通过文章id得到文章内容


@require_http_methods(["GET"])
def GetArticleContentById(request):
    response = {}
    try:
        id = request.GET.get("id", 0)
        AddHit(id)
        ip = get_ip(request)
        Content = models.AritcleDatils.objects.filter(ArticleId_id=int(id))
       
        Article = models.Article.objects.filter(Id=int(id))
        Content = json.loads(serializers.serialize("json", Content))
        # this is markdown  vue前台使用解码 这里不需要解码
        
        # con=Content[0]['fields']['Content']
        # if con[0:3] != "<br":
        #     Content[0]['fields']['Content'] = markdown.markdown(con.replace("\r\n", '  \n'), extensions=[
        #         'markdown.extensions.extra',
        #         'markdown.extensions.codehilite',
        #         'markdown.extensions.toc',
        #     ], safe_mode=True, enable_attributes=False)
        
        # end

        Article = json.loads(serializers.serialize("json", Article))
        response['Article'] = Article
        response['Content'] = Content

        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def GetCommentsByArticleId(request):
    response = {}
    try:
        id = request.POST.get("id", 0)
        comments = models.Comment.objects.filter(ArticleId_id=int(id))
        response['Comments'] = json.loads(
            serializers.serialize("json", comments))

        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def AddHit(ArticleId):
    try:
        article = models.Article.objects.get(Id=int(ArticleId))
        article.Hits = article.Hits+1
        article.save()
    except Exception as e:
        return False
    return True


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    return ip


@require_http_methods(["POST"])
def AddLikeNum(request):
    response = {}
    try:
        id = request.POST.get("id", 0)
        judge = request.POST.get("is", 0)
        agent = request.META.get('HTTP_USER_AGENT', "NULL")
        ip = get_ip(request)
        response["ip"] = ip

        if (models.UserBehavior.objects.filter(ArticleId_id=int(id), UserAgent=agent, IP=ip).count() == 0) :
            if judge == 0:  # 判断是否为获取点赞信息而不是增加点赞
                Article = models.Article.objects.get(
                    Id=int(id))  # madmin 数据库问题 导致无法使用触发器。
                Article.Likenum = Article.Likenum+1
                models.UserBehavior.objects.create(  # UserAgent
                    IP=ip, UserAgent=agent, Type="1", ArticleId_id=int(id))  # 创建用户行为引发触发器增加likenum
                Article.save()
            response["return"] = "1"
        else:
            response["return"] = "0"
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
        response["return"] = "1"
    return JsonResponse(response)


HeaderPath = [
    "/static/images/CommentHeader/rabbit.jpg",
    "/static/images/CommentHeader/bear.jpg",
    "/static/images/CommentHeader/smile.jpg",
    "/static/images/CommentHeader/girl.jpg",
    "/static/images/CommentHeader/rhizomys.jpg",
    "/static/images/CommentHeader/duck.jpg",
]


@require_http_methods(["POST"])
def AddComment(request):
    response = {}
    try:
        id = request.POST.get("ArticleId")
        agent = request.META.get('HTTP_USER_AGENT', None)
        ip = get_ip(request)
        header = request.POST.get("UserHeader")
        if header == "null":
            header = random.sample(HeaderPath, 1)[0]
        
        comment=models.Comment( ArticleId_id=int(id),
            UserName=request.POST.get("UserName"),
            PersonalBlog=request.POST.get("PersonalBlog"),
            Content=request.POST.get("Content"),
            UserEmail=request.POST.get("UserEmail"),
            UserHeader=header)
        comment.save()
        
        # models.Comment.objects.create(
        #     ArticleId_id=int(id),
        #     UserName=request.POST.get("UserName"),
        #     PersonalBlog=request.POST.get("PersonalBlog"),
        #     Content=request.POST.get("Content"),
        #     UserEmail=request.POST.get("UserEmail"),
        #     UserHeader=header)

        models.UserBehavior.objects.create(
            IP=ip, UserAgent=agent, Type="2", CommentId_id=comment.Id, ArticleId_id=int(id))  # 创建用户行为
        response["return"] = 1
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
        response["return"] = 0
    return JsonResponse(response)
