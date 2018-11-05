from django.db import models
from datetime import datetime 
from DjangoUeditor.models import UEditorField

#类别表
class Category(models.Model):
  CategoryName=models.CharField(max_length=50,verbose_name="分类名")
  BackgroundPath=models.CharField(max_length=100,verbose_name='背景地址' )
  CategoryLog=models.CharField(max_length=100,null=True,verbose_name='Log地址' )
  Intor=models.CharField(max_length=500,null=True,verbose_name='分类详情')
  Id=models.AutoField(primary_key=True,verbose_name='类ID')

  class Meta:
    verbose_name='类别'
    verbose_name_plural = verbose_name 

  def __str__(self):
    return self.CategoryName


#创建Article表
class Article(models.Model):
  CategoryId=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='外键类名id') #练级删除，主表数据删除时从表数据也删除
  ArticleName=models.CharField(max_length=50,verbose_name='文章名')
  BackgroundPath=models.CharField(max_length=100,verbose_name='文章背景地址')
  #ArticleSuggests=models.CharField(max_length=500,null=True,verbose_name='文章详情')
  PostedTime=models.DateTimeField(default=datetime.now,verbose_name='发表时间')
  Hits=models.IntegerField(verbose_name='点击数')
  Likenum=models.IntegerField(verbose_name='点赞数')
  Id=models.AutoField(primary_key=True,verbose_name='文章ID')
  class Meta:
    verbose_name='文章'
    verbose_name_plural = verbose_name 

  def __str__(self):
    return self.ArticleName


#创建文章详情表
class AritcleDatils(models.Model):
  ArticleId=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name='外键文章id')
  Content=UEditorField(height=300,width=300,default='',blank=True,toolbars='besttome',
  verbose_name="文章内容",
  imagePath="./images/",
  filePath="./files/",
  upload_settings={"imageMaxSize":1204000})
  LastDataChange=models.DateTimeField(default=datetime.now,verbose_name='最后修改时间')
  class Meta:
    verbose_name='文章详情'
    verbose_name_plural = verbose_name 

  def __str__(self):
    return self.ArticleId


'''
Content=UEditorField(height=300,width=300,default='',blank=True,imagePath='./images/',toolbars='besttome'
  
UEditorField继承自models.TextField,因此你可以直接将model里面定义的models.TextField直接改成UEditorField即可。<br>
UEditorField提供了额外的参数：<br>
toolbars:配置你想显示的工具栏，取值为mini,normal,full,besttome, 代表小，一般，全部,涂伟忠贡献的一种样式。如果默认的工具栏不符合您的要求，您可以在settings里面配置自己的显示按钮。参见后面介绍。<br>
imagePath:图片上传的路径,如"images/",实现上传到"{{MEDIA_ROOT}}/images"文件夹<br>
filePath:附件上传的路径,如"files/",实现上传到"{{MEDIA_ROOT}}/files"文件夹<br>
scrawlPath:涂鸦文件上传的路径,如"scrawls/",实现上传到"{{MEDIA_ROOT}}/scrawls"文件夹,如果不指定则默认=imagepath<br>
imageManagerPath:图片管理器显示的路径，如"imglib/",实现上传到"{{MEDIA_ROOT}}/imglib",如果不指定则默认=imagepath。<br>
options：其他UEditor参数，字典类型。参见Ueditor的文档ueditor_config.js里面的说明。<br>
css:编辑器textarea的CSS样式<br>
width，height:编辑器的宽度和高度，以像素为单位。<br>
'''
