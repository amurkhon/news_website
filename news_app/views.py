from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView,DetailView,TemplateView
from .models import News,Category
from .forms import ContactForm
# Create your views here.

class NewsListView(ListView):
  model = News
  template_name = 'news_list.html'
  context_object_name = 'news'

  def get_queryset(self):
    return News.objects.filter(status=News.Status.Published)

class NewsListDetail(DetailView):
  model = News
  template_name = 'news_detail.html'
  

# def indexView(request):
#   categories = Category.objects.all()
#   news_list = News.published.all()
#   news_one = News.objects.filter(category__name='iqtisodiyot')[:1]
#   news_others = News.objects.filter(category__name='iqtisodiyot')[1:5]

#   context = {
#     "news_list":news_list,
#     "categories":categories,
#     "news_one":news_one,
#     "news_others":news_others
#   }
#   return render(request, 'index.html',context=context)

class IndexView(ListView):

  model = News
  template_name = 'index.html'
  context_object_name = 'news'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context =  super().get_context_data(**kwargs)
    context['categories'] = Category.objects.all()
    context['news_list'] = News.published.all()
    context['finance'] = News.objects.filter(category__name='iqtisodiyot').order_by('-pulished_time')
    context['world'] = News.objects.filter(category__name='jahon').order_by('-pulished_time')
    context['technology'] = News.objects.filter(category__name='fan-texnika').order_by('-pulished_time')
    context['sport'] = News.objects.filter(category__name='sport').order_by('-pulished_time')

    return context
  
class WorldNewsView(ListView):
  model = News
  template_name = 'jahon.html'
  context_object_name = 'jahon_yangiliklari'

  def get_queryset(self) -> QuerySet[Any]:
    news = self.model.published.all().filter(category__name = 'jahon')
    return news

class TechnologyNewsView(ListView):
  model = News
  template_name = 'fan-texnika.html'
  context_object_name = 'texnika_yangiliklari'

  def get_queryset(self) -> QuerySet[Any]:
    news = self.model.published.all().filter(category__name = 'fan-texnika')
    return news

class SportNewsView(ListView):
  model = News
  template_name = 'sport.html'
  context_object_name = 'sport_yangiliklari'

  def get_queryset(self) -> QuerySet[Any]:
    news = self.model.published.all().filter(category__name = 'sport')
    return news

class FinanceNewsView(ListView):
  model = News
  template_name = 'iqtisodiyot.html'
  context_object_name = 'iqtisodiy_yangiliklari'

  def get_queryset(self) -> QuerySet[Any]:
    news = self.model.published.all().filter(category__name = 'iqtisodiyot')
    return news
  

# def contactPageView(request):
#   form = ContactForm(request.POST)
#   if request.method == "POST" and form.is_valid():
#     form.save()
#     return HttpResponse("<h2> Biz bilan bog'langaniz uchun tashakkur!")
#   context = {
#     "form":form
#   }
#   return render(request, 'contact.html',context )

class contactPageView(TemplateView):
  template_name = "contact.html"

  def get(self,request,*args,**kwargs):
    form = ContactForm()
    context = {
      "form":form
    }
    return render(request, "contact.html", context)
  
  def post(self,request,*args,**kwargs):
    form = ContactForm(request.POST)
    if request.method == "POST" and form.is_valid():
      form.save()
      return HttpResponse("<h2> Biz bilan bog'langaniz uchun tashakkur!")
    context = {
      "form":form
    }
    return render(request, "contact.html",context)



def Error_404(request):
  context = {
    
  }
  return render(request,'404.html',context)

