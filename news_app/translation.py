from modeltranslation.translator import register, TranslationOptions, translator
from .models import News, Category

# 1-chi usul
class NewsTranslationOptions(TranslationOptions):
  fields = ('title','body')

# 2-chi usul
translator.register(News, NewsTranslationOptions)

class CategoryTranslationOptions(TranslationOptions):
  fields = ('name',)

translator.register(Category, CategoryTranslationOptions)

