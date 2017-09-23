from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^login/$', views.login, name='blog_login'),
    url(r'^logout/$', views.logout, name='blog_logout'),
    url(r'^admin_page/$', views.admin_page, name='admin_page'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^category/(?P<category_slug>[\w-]+)/$', views.post_by_category, name='post_by_category'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_by_tag, name='post_by_tag'),
    url(r'^tag/(?P<author>[\w-]+)/$', views.post_by_tag, name='post_by_tag'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^$', views.post_list, name='post_list'),
]