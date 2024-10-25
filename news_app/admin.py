from django.contrib import admin
from .models import News, Category, Contact, Comment

# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
  list_display = ['title','slug','pulished_time','status']
  list_filter = ['status','created_time','pulished_time']
  prepopulated_fields = {'slug':('title',)}
  date_hierarchy = 'pulished_time'
  search_fields = ['title','body']
  ordering = ['status','pulished_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display =['id','name']

admin.site.register(Contact)

class CommentAdmin(admin.ModelAdmin):
  list_display = ['user','body','created_time','active']
  list_filter = ['created_time','active']
  search_fields = ['user','body']
  actions = ['disabled_comment','activate_comment']
  def disabled_commnet(self, request, queryset):
    queryset.update(active=False)

  def active_comment(self, reuqest, queryset):
    queryset.update(active=True)

admin.site.register(Comment, CommentAdmin)