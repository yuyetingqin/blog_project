# *_* coding: utf-8 *_*

from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from blog.models import Article, Tag, Comment, Catagory, User, Ad, Links
# Create your views here.


# 全局返回信息，所有页面共有
def global_info(request):
    # 网站标题及描述
    site_title = settings.SITE_TITLE
    site_desc = settings.SITE_DESC
    # 广告信息 查询最新6条
    ad_img = Ad.objects.all().order_by("-id")[:6]
    # 标签云信息
    tag_list = Tag.objects.all()
    # 友情链接信息
    link_list = Links.objects.all()

    return locals()


# 首页
def index(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list, settings.PAGE_NUM)

    try:
        page = request.GET.get("page", 1)
        print page
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)

    return render(request, "index.html", locals())

