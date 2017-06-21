from django.conf.urls import include, url
from django.contrib import admin
from blog.views import index, article, article_list
from django.conf import settings
from blog.upload import upload_image

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url("^uploads/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.MEDIA_ROOT,}),

    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name="upload_image"),

    url(r'^$', index, name="index"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/(\d+)$', article, name="article"),
    url(r'^tag/(\d+)$', article_list, name="article_list"),

]
