from django.contrib import admin
from .models import News, Category, Contact

# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
  list_display = ['title','slug','pulished_time','status']
  list_filter = ['status','created_time','pulished_time']
  prepopulated_fields = {"slug":('title',)}
  date_hierarchy = 'pulished_time'
  search_fields = ['title','body']
  ordering = ['status','pulished_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display =['id','name']

admin.site.register(Contact)