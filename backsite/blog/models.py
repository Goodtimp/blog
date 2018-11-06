# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField

# 类别表
class Category(models.Model):
    CategoryName = models.CharField(max_length=10, verbose_name="分类名")
    BackgroundPath = models.CharField(max_length=50, verbose_name="背景地址")
    CategoryLog = models.CharField(max_length=50, null=True, verbose_name="Log地址")
    Intor = models.CharField(max_length=200, null=True, verbose_name="分类详情")
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
    ArticleName = models.CharField(max_length=20, verbose_name="文章名")
    BackgroundPath = models.CharField(max_length=50, verbose_name="文章背景地址")
    ArticleSuggests = models.CharField(max_length=200, null=True, verbose_name="文章详情")
    PostedTime = models.DateTimeField(default=datetime.now, verbose_name="发表时间")
    Hits = models.IntegerField(verbose_name="点击数")
    Likenum = models.IntegerField(verbose_name="点赞数")
    Id = models.AutoField(primary_key=True, verbose_name="文章ID")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ArticleName


# 创建文章详情表
class AritcleDatils(models.Model):
    Content = UEditorField(
        verbose_name="文章内容",
        height=500,
        width=900,
        max_length=102400,
        default=u"开始一篇新的文章",
        blank=True,
        imagePath="./images/",
        toolbars="besttome",
        filePath="./files/",
    )
    ArticleId = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name="外键文章id"
    )
    LastDataChange = models.DateTimeField(default=datetime.now, verbose_name="最后修改时间")

    class Meta:
        verbose_name = "文章详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.ArticleId)

