# -*- coding: utf-8 -*-
from xadmin import views
import xadmin
from . import models


class BaseSetting(object):
  """xadmin的基本配置"""
  enable_themes = True  # 开启主题切换功能
  use_bootswatch = True

class GlobalSettings(object):
  """xadmin的全局配置"""
  site_title = "722个人博客"  # 设置站点标题
  site_footer = "blog"  # 设置站点的页脚
  menu_style = "accordion"  # 设置菜单折叠
 

class CategoryAdmin(object):
  #后台展示字段
  list_display=['CategoryName','BackgroundPath','CategoryLog','Intor','Id']
  #可用于查找的字段
  search_fields=['Id','CategoryName']
  #可直接编辑的字段
  list_editable=['CategoryName','BackgroundPath','CategoryLog','Intor']

class ArticleAdmin(object):
  #后台展示字段
  list_display=['CategoryId','ArticleName','BackgroundPath','ArticleSuggests','PostedTime','Hits','Likenum','Id']
  search_fields=['Id','CategoryId','ArticleName']
  list_editable=['ArticleName','BackgroundPath','ArticleSuggests']

class AritcleDatilsAdmin(object):
  #后台展示字段
  list_display=['ArticleId','LastDataChange','Content']
  search_fields=['ArticleId']
  list_editable=['Content']
  style_fields={'Content':'ueditor'}
 
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(models.Category,CategoryAdmin)
xadmin.site.register(models.Article,ArticleAdmin)
xadmin.site.register(models.AritcleDatils,AritcleDatilsAdmin)
