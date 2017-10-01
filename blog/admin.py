from django.contrib import admin
from django.contrib import admin
from blog import models

# Register your models here.


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('name', 'email', 'subject', 'message')
        return self.readonly_fields

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on')
    search_fields = ['name', 'email']
    ordering = ['-name']
    list_filter = ['active']
    date_hierarchy = 'created_on'
    fields = ('firstname', 'lastname', 'author_info', 'email')



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'author', 'category',)
    search_fields = ['title', 'content', 'author', 'category', 'tags']
    ordering = ['-publication_date']
    list_filter = ['publication_date']
    date_hierarchy = 'publication_date'
    filter_horizontal = ('tags',)
    raw_id_fields = ('author', 'tags',)
    fields = ('title', 'content', 'author', 'category', 'tags', 'file')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)
    fields = ('name', 'author',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)
    fields = ('name', 'author',)


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Feedback, FeedbackAdmin)
