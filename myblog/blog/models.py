from django.db import models

# Create your models here.
# 标签类
class Tag(models.Model):
  tag_name = models.CharField(max_length=20)
  create_time = models.DataTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.tag_name
  
  
  # 分类类
class Classification(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
      return self.name
    
    
   # 作者类
class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    
    def __str__(self):
      retrun u'%s' %(self.name)
      
      
# 文章类
class Article(models.Model):
    # 文章标题
    caption = models.CharField(max_length=30)
    subcaption = models.CharField(max_length=50, blank=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    classification = models.ForeignKey(Classification, on_delete=models.CASSCADE)
    tages = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    
