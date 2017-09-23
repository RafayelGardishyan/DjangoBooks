from django.contrib import admin
from django.contrib import admin
from blog import models

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on')
    search_fields = ['name', 'email']
    ordering = ['-name']
    list_filter = ['active']
    date_hierarchy = 'created_on'



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'author', 'category',)
    search_fields = ['title', 'content', 'author']
    ordering = ['-publication_date']
    list_filter = ['publication_date']
    date_hierarchy = 'publication_date'
    filter_horizontal = ('tags',)
    raw_id_fields = ('tags',)
    fields = ('title', 'content', 'author', 'category', 'tags', 'file')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Feedback, FeedbackAdmin)
