# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField
from backsite.settings import MEDIA_URL
# 类别表

# this is markdown
from mdeditor.fields import MDTextField #必须导入


class Category(models.Model):
    CategoryName = models.CharField(max_length=50, verbose_name="分类名")
    BackgroundPath = models.ImageField(
        upload_to="images/category_back", null=True, verbose_name="背景地址", max_length=255)
    # BackgroundPath = models.ImageField(max_length=50, verbose_name="背景地址")
    CategoryLog = models.ImageField(
        upload_to="images/category_log", null=True, max_length=255, verbose_name="Log地址")
    # CategoryLog = models.CharField(max_length=50, null=True, verbose_name="Log地址")
    Intor = models.CharField(max_length=500, null=True, verbose_name="分类详情")
    Id = models.AutoField(primary_key=True, verbose_name="类ID")

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.CategoryName


# 创建Article表
class Article(models.Model):
    CategoryId = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="外键类名id"
    )  # 练级删除，主表数据删除时从表数据也删除
    ArticleName = models.CharField(max_length=300, verbose_name="文章名")
    BackgroundPath = models.ImageField(
        upload_to="images/article_img", null=True, verbose_name="文章背景地址", max_length=255)
   # BackgroundPath = models.CharField(max_length=50, verbose_name="文章背景地址")
    ArticleSuggests = models.CharField(
        max_length=300, null=True, verbose_name="文章详情")
    PostedTime = models.DateTimeField(
        default=datetime.now, verbose_name="发表时间")
    Hits = models.IntegerField(verbose_name="点击数", default=1)
    Likenum = models.IntegerField(verbose_name="点赞数", default=0)
    Id = models.AutoField(primary_key=True, verbose_name="文章ID")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ArticleName


# 创建文章详情表
class AritcleDatils(models.Model):
    # Content = UEditorField(
    #     verbose_name="文章内容",
    #     height=500,
    #     width=900,
    #     max_length=102400,
    #     default=u"开始一篇新的文章",
    #     blank=True,
    #     imagePath="./images/",
    #     toolbars="besttome",
    #     filePath="./files/",
    # )
    Content=MDTextField()

    ArticleId = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name="外键文章id"
    )
    LastDataChange = models.DateTimeField(
        default=datetime.now, verbose_name="最后修改时间")

    class Meta:
        verbose_name = "文章详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.ArticleId)

#评论表
class Comment(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="评论ID")
    ArticleId= models.ForeignKey(Article, on_delete=models.CASCADE, null=True, verbose_name="外键文章id") 
    UserName=models.CharField(max_length=300, verbose_name="用户姓名")
    UserHeader=models.CharField(max_length=300, null=True, verbose_name="评论用户头像",default="/static/images/CommentHeader.jpg")
    UserEmail=models.EmailField(max_length=254,null=True, verbose_name="用户Email")
    Content=models.CharField(max_length=5000, verbose_name="评论内容")
    PostedTime=models.DateTimeField(default=datetime.now, verbose_name="评论时间")
    Likenum= models.IntegerField(verbose_name="点赞数", default=0)
    PersonalBlog=models.CharField(max_length=300, verbose_name="个人博客链接",default="#")
    class Meta:
        verbose_name="评论"

    def __str__(self):
        return self.UserName

#用户行为表
class UserBehavior(models.Model):
    IP=models.CharField(max_length=300, verbose_name="用户ip")
    UserAgent=models.CharField(max_length=500, verbose_name="用户设备信息",null=True)
    Type=models.IntegerField(default=1,verbose_name="行为类型类型,1喜欢,2评论,3评论点赞")
    ArticleId= models.ForeignKey(Article, on_delete=models.CASCADE, null=True, verbose_name="外键文章id") 
    CommentId=models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, verbose_name="外键评论id") 
    Time=models.DateTimeField(default=datetime.now, verbose_name="行为时间")
    class Meta:
        verbose_name="用户行为"

    def __str__(self):
        return self.Type


 
