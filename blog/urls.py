from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^category/(?P<category_slug>[\w-]+)/$', views.posts_by_category, name='post_by_category'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.posts_by_tag, name='post_by_tag'),
    url(r'^tag/(?P<author>[\w-]+)/$', views.posts_by_tag, name='post_by_tag'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^$', views.post_list, name='post_list'),
]