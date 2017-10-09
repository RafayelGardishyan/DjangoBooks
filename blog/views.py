from functools import reduce
from django.forms.models import model_to_dict
from django.core.mail import mail_admins, send_mail
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Post, Author, Tag, Category
from .forms import FeedbackForm
from django_books import helpers
from django.contrib import auth, messages


def index(request):
    return HttpResponse("Hello Django")

def post_list(request):
    post_list = Post.objects.order_by("-id").all()
    posts = helpers.pg_records(request, post_list, 10)
    return render(request, 'blog/post_list.html', {'posts': posts})

def author_list_letter(request, letter):
    author_list = Author.objects.order_by("-name").all().filter(name__startswith=letter)
    # print(author_list)
    # for author in author_list:
    #     print(author)
    #     first = author.first_letter()
    #     print(first)
    #     if not first == letter:
    #         print(letter)
    #         print(author)
    #         author_list.exclude(author)

    authors = helpers.pg_records(request, author_list, 10)
    return render(request, 'blog/author_list_letter.html', {'authors': authors, 'letter': letter})

def api_authors(request):
    authorslist_raw = list(Author.objects.values('id'))
    authorlist = {}
    for item in authorslist_raw:
        link = Author.objects.get(id=item['id']).get_absolute_url_api()
        name = Author.objects.get(id=item['id']).name
        authorlist[name] = {'id': item['id'], 'url': link, }

    return JsonResponse(authorlist)

def api_authors_single(request, author_name):
    try:
        author = Author.objects.get(id=author_name)
    except Author.DoesNotExist:
        return HttpResponseNotFound("Page not found")
    print(author_name)
    authorlist = {}
    name = author.name
    info = author.author_info
#     booksraw = Post.objects.get(author=author)
#     books = Post.objects.values('title')
#     from django.core import serializers
#     books = serializers.serialize('json', Post.objects.get(author=author), fields=('title',))
    
    
    authorlist[name] = {'id': author.id, 'name': name, 'info': info}

    return JsonResponse(authorlist)

def api_books_single(request, pk):
    try:
        book = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponseNotFound("Page not found")
    authorlist = {}
    id = post.id
    name = post.name
    author = post.author
    info = author.content
    dwnldlink = author.file.url
    
#     booksraw = Post.objects.get(author=author)
#     books = Post.objects.values('title')
#     from django.core import serializers
#     books = serializers.serialize('json', Post.objects.get(author=author), fields=('title',))
    
    
    authorlist[name] = {'id': id, 'name': name, 'author': author 'info': info, 'downloadlink': dwnldlink}

    return JsonResponse(authorlist)

def api_books(request):
    authorslist_raw = list(Post.objects.values('id'))
    authorlist = {}
    for item in authorslist_raw:
        author = Post.objects.get(id=item['id']).author
        link = Post.objects.get(id=item['id']).get_absolute_url_api()
        downloadlink = Post.objects.get(id=item['id']).file.url
        name = Post.objects.get(id=item['id']).title
        authorlist[name] = {'id': item['id'], 'title': name, 'author': author, 'url': link, 'download_link': downloadlink }

    return JsonResponse(authorlist)

def author_list(request):
    author_list = Author.objects.order_by("-name").all()
    authors = helpers.pg_records(request, author_list, 10)
    return render(request, 'blog/author_list.html', {'authors': authors})

def category_list(request):
    category_list = Category.objects.order_by("-name").all()
    categoies = helpers.pg_records(request, category_list, 10)
    return render(request, 'blog/category_list.html', {'categories': categoies})

def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponseNotFound("Page not found")

    return render(request, 'blog/post_detail.html', {'post': post})

def author_info(request, author_name):
    try:
        author = Author.objects.get(slug=author_name)
    except Author.DoesNotExist:
        return HttpResponseNotFound("Page not found")

    return render(request, 'blog/author_detail.html', {'author': author})

def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), category=category)
    posts = helpers.pg_records(request, posts, 10)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/post_by_category.html', context)


# view function to display post by tag
def post_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), tags=tag)
    posts = helpers.pg_records(request, posts, 10)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/post_by_tag.html', context )

def post_by_author(request, author_name):
    author = get_object_or_404(Author, slug=author_name)
    posts = get_list_or_404(Post.objects.order_by("-id"), author=author)
    posts = helpers.pg_records(request, posts, 10)
    context = {
        'author': author,
        'posts': posts
    }
    return render(request, 'blog/post_by_author.html', context )


def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            sender = f.cleaned_data['email']
            subject = "You have a new Feedback from {}:{}".format(name, sender)
            message = "Subject: {}\n\nMessage: {}".format(f.cleaned_data['subject'], f.cleaned_data['message'])

            mail_admins(subject, message)
            f.save()
            return render(request, 'blog/thank_you.html', {'name' : name})

    else:
        f = FeedbackForm()
    return render(request, 'blog/feedback.html', {'form': f})

def login(request):
    if request.user.is_authenticated():
        return redirect('admin_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('admin_page')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'blog/login.html')


def logout(request):
    auth.logout(request)
    return render(request,'blog/logout.html')


def admin_page(request):
    if not request.user.is_authenticated():
        return redirect('blog_login')

    return render(request, 'blog/admin_page.html')
