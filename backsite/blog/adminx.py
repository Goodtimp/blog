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
  list_display=['CategoryId','ArticleName','Hidden','BackgroundPath','ArticleSuggests','PostedTime','Hits','Likenum','LastDataChange','Id']
  search_fields=['Id','CategoryId','ArticleName','Hidden']
  list_editable=['ArticleName','BackgroundPath','Hidden','ArticleSuggests']


class CommentAdmin(object):
  #后台展示字段
  list_display=['Id','ArticleId','UserName','PersonalBlog','UserEmail','Content','PostedTime','Likenum']
  search_fields=['Id','ArticleId','UserName','PersonalBlog','UserEmail','PostedTime','Likenum']

class UserBehaviorAdmin(object):
  #后台展示字段
  list_display=['IP','Type','ArticleId','Time']
  search_fields=['IP','Type','ArticleId','Time']
 
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(models.Category,CategoryAdmin)
xadmin.site.register(models.Article,ArticleAdmin)
xadmin.site.register(models.Comment,CommentAdmin)
xadmin.site.register(models.UserBehavior,UserBehaviorAdmin)
