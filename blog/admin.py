# *-* coding: utf-8 *-*
from django.contrib import admin
from blog.models import Tag, Catagory, Comment, Article, Ad, Links, User

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    fields = ("name",)
    list_display = ("name",)

admin.site.register(Tag, TagAdmin)

admin.site.register(Catagory)

admin.site.register(Comment)


class ArticleAdmin(admin.ModelAdmin):
    # fields = ("name",)
    list_display = ("title","date_publish", "category")

    class Media:
        js = (
            "/static/js/kindeditor-4.1.7/kindeditor-min.js",
            "/static/js/kindeditor-4.1.7/lang/zh_CN.js",
            "/static/js/kindeditor-4.1.7/themes/simple/simple.css",
            "/static/js/kindeditor-4.1.7/config.js",
        )

admin.site.register(Article, ArticleAdmin)

admin.site.register(Ad)

admin.site.register(Links)

admin.site.register(User)
