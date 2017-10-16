from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="Author Name")
    slug = models.SlugField(max_length=100)
    email = models.EmailField( blank=True)
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_logged_in = models.DateTimeField(auto_now=True)
    author_info = models.TextField(max_length=1000, verbose_name="Author Info")


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_by_author', args=[self.slug])
    
    def get_absolute_url_api(self):
        return reverse('Api/Authors/Single', args=[self.id])

    def get_absolute_url_info(self):
        return reverse('author_info', args=[self.slug])

    def first_letter(self):
        return self.name[0]


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_by_category', args=[self.slug])

    def first_letter(self):
        return self.name[0]
    
#     def get_absolute_url_api(self):
#         return reverse('Api/Authors/Single', args=[self.id])


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_by_tag', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)
        
   


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    file = models.FileField(upload_to='books_storage')


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])
    
    def get_absolute_url_api(self):
        return reverse('Api/Books/Single', args=[self.id]) 

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" +  self.email

class SubmitBook(models.Model):
    submitter = models.CharField(max_length=200, verbose_name="Your name")
    submitteremail = models.EmailField(max_length=200, verbose_name="Your E-mail")
    booktitle = models.CharField(max_length=200, verbose_name="Book title")
    bookauthor = models.CharField(max_length=200, verbose_name="Book author")
    bookdescription = models.TextField(verbose_name="Book Description")
    date = models.DateField(auto_now_add=True)
    thefile = models.FileField(upload_to="submissions",verbose_name="Book file")


    class Meta:
        verbose_name_plural = "Book Submission"

    def __str__(self):
        return self.booktitle + "-" + self.submitter
