# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from io import BytesIO
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your models here.

# 用户模型
class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatar/%Y/%d", default="avatar/default.jpgmak", max_length=200)
    qq = models.CharField(max_length=15, blank=True, null=True, verbose_name="qq号")
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name="手机号")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name="标签名称", null=False)


    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name




# 文章分类
class Catagory(models.Model):
    name = models.CharField(max_length=30, verbose_name="分类名称")
    index = models.IntegerField(default=999, verbose_name="分类排序")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name



#文章模型
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="文章标题")
    desc = models.CharField(max_length=50, verbose_name="文章描述")
    content = models.TextField(verbose_name="文章内容")
    click_count = models.IntegerField(default=0, verbose_name="点击次数")
    is_recommend = models.BooleanField(default=False, verbose_name="是否推荐")
    image_url = models.ImageField(default="article/default.jpg", upload_to="article/%Y/%m", max_length=150, verbose_name="文章图片")
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    user = models.ForeignKey(User, verbose_name="用户")
    category = models.ForeignKey(Catagory, blank=True, null=True, verbose_name="分类")
    tag = models.ManyToManyField(Tag, verbose_name="标签")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ["-date_publish"]

    def __unicode__(self):
        return self.title

    def save(self):
        # Opening the uploaded image
        im = Image.open(self.image_url)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((245, 200))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image_url = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image_url.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(Article, self).save()

#评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name="评论内容")
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    user = models.ForeignKey(User, blank=True, null=True, verbose_name="用户")
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name="文章")
    pid = models.ForeignKey("self", blank=True, null=True, verbose_name="父级评论")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        ordering = ["-date_publish"]

    def __unicode__(self):
        return str(self.id)



#广告
class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name="广告标题")
    description = models.CharField(max_length=200, verbose_name="广告描述")
    image_url = models.ImageField(upload_to="ad/%Y/%m", verbose_name="图片路径")
    callback_url = models.URLField(null=True, blank=True, verbose_name="回调url")
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    index = models.IntegerField(default=999, verbose_name="广告排序")

    class Meta:
        verbose_name = "广告"
        verbose_name_plural = verbose_name
        ordering = ["index", "id"]

    def __unicode__(self):
        return self.title


    def save(self):
        # Opening the uploaded image
        im = Image.open(self.image_url)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((670, 280))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image_url = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image_url.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(Ad, self).save()


#友情链接
class Links(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    description = models.CharField(max_length=200, verbose_name="友情链接")
    callback_url = models.URLField(verbose_name="url地址")
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    index = models.IntegerField(default=999, verbose_name="排序(从小到大)")

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name
        ordering = ["index", "-id"]

    def __unicode__(self):
        return self.title

