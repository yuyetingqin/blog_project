# *_* coding: utf-8 *_*

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
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

    # 图文推荐
    tuwen_list = Article.objects.all().order_by("-date_publish")[:6]

    #点击排行榜
    article_list = Article.objects.all().order_by("-click_count")[:6]

    return locals()


# 首页
@login_required(login_url='/login/')
def index(request):
    print request.user.is_authenticated()
    article_list = Article.objects.all()

    paginator = Paginator(article_list, settings.PAGE_NUM)

    try:
        page = request.GET.get("page", 1)
        # print page
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)

    paginator_list = article_list

    return render(request, "index.html", locals())


# 文章详情显示
def article(request, article_id):

    article_info = Article.objects.get(id=article_id)
    article_info.click_count = article_info.click_count + 1
    article_info.save()

    return render(request, "article.html", locals())


# 对应标签下的文章列表
def article_list(request, tag_id):
    tag_id = tag_id
    if tag_id == "0":
        tag_info = Article.objects.all()
    else:
        tag_info = Tag.objects.get(id=tag_id)

    return render(request, "article_list.html", locals())


#首页登录
def login_site(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print "username:%s, password:%s" % (username, password)
    user = authenticate(username=username, password=password)
    if user is not None :
        if user.is_active:
            login(request, user)
            print "登录验证成功!"
            return redirect("/")
        else:
            return render(request, "login.html", {"error" : "该用户未激活!"})
    else:
        if username == "":
            msg = "请输入账号和密码!"
        else:
            msg = "用户名或密码错误，请重新输入!"
        return render(request, "login.html", {"error" : msg })


#登出
def logout_site(request):
    logout(request)
    return redirect("/login/")


#注册
def register_site(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password1', '').strip()
        password2 = request.POST.get('password2', '').strip()
        email = request.POST.get('email', '')
        mobile = request.POST.get('phone', '')

        if username != '' and password == password2 and email != '' and mobile != '':
            user = User.objects.create_user(username=username, password=password, mobile=mobile, email=email)
            user.save()
            return redirect("/login/")

        else:
            return render(request, "register.html", )
    return render(request, "register.html", )



