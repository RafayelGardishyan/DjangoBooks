from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^login/$', views.login, name='blog_login'),
    url(r'^logout/$', views.logout, name='blog_logout'),
    url(r'^admin_page/$', views.admin_page, name='admin_page'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^category/(?P<category_slug>[\w-]+)/$', views.post_by_category, name='post_by_category'),
    url(r'^author/(?P<author_name>[\w-]+)/books$', views.post_by_author, name='post_by_author'),
    url(r'^author/(?P<author_name>[\w-]+)/info$', views.author_info, name='author_info'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_by_tag, name='post_by_tag'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^authors/$', views.author_list, name='author_list'),
    url(r'^authors/(?P<letter>\w+)$', views.author_list_letter, name='author_list_letter'),
    url(r'^categories/$', views.category_list, name='category_list'),
    url(r'api/authors/$', views.api_authors, name='Api/Authors'),
    url(r'api/books/$', views.api_books, name='Api/Books'),
    url(r'^api/books/(?P<pk>\d+)/$', views.api_books_single, name='Api/Books/Single'),
    url(r'^author/(?P<author_name>[\w-]+)$', views.api_authors_single, name='Api/Authors/Single')
]
