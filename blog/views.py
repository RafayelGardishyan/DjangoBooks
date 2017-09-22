from django.http import HttpResponse, HttpResponseNotFound,Http404
from django.shortcuts import render
from .models import Post, Author, Tag, Category

def index(request):
    return HttpResponse("Hello Django")

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponseNotFound("Page not found")

    return render(request, 'blog/post_detail.html', {'post': post})

def posts_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category__slug=category_slug)
    context = {
        'category': category,
        'posts': posts
    }
    print(category)
    return render(request, 'blog/post_by_category.html', context)


# view function to display post by tag
def posts_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags__name=tag)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/post_by_tag.html', context )

