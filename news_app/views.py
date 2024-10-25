from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render, HttpResponse,get_object_or_404
from django.views.generic import ListView,TemplateView, UpdateView, DeleteView,CreateView,DetailView
from django.urls import reverse_lazy
from config.custom_permissions import OnlyLoggedSuperUser
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import News,Category,Comment
from .forms import ContactForm, CommentForm
from django.db.models import Q
from hitcount.views import HitCountDetailView
# Create your views here.

  
class NewsDetailView(HitCountDetailView ,LoginRequiredMixin, DetailView):
  model = News
  template_name = 'news_detail.html'
  context_object_name = 'news'
  count_hit = True

   
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['comments'] = self.object.comments.filter(active=True)
    context['comment_form'] = CommentForm()
    return context
  def post(self, request, *args, **kwargs):
        news = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = news
            new_comment.user = request.user
            new_comment.save()
            return redirect(news.get_absolute_url())
        context = {'news': news, 'comments': news.comments.filter(active=True), 'comment_form': comment_form,'new_comment':new_comment,}
        return render(request, 'news_detail.html', context)

# class PostCountHitDetailView(HitCountDetailView, DeleteView):
#     model = News        # your model goes here
#     count_hit = True   # set to True if you want it to try and count the hit
#     context_object_name = 'news'

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

class UpdateNewsView(OnlyLoggedSuperUser, UpdateView):
  model = News
  fields = ('title','image','body','category')
  template_name = 'crud/news_update.html'

class DeleteNewsView(OnlyLoggedSuperUser, DeleteView):
  model = News
  template_name = 'crud/news_delete.html'
  success_url = reverse_lazy('home_page')

class CreateNews(OnlyLoggedSuperUser, CreateView):
  model = News
  fields = ('title','slug','image','body','category','status')
  template_name = 'crud/news_create.html'

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

class CommentsView(TemplateView):
  template_name="crud/news_comments.html"

  def get(self,request, *args,**kwargs):
    form = CommentForm()

    context = {
      'form':form
    }
    return render(request, "crud/news_comments.html", context)
  
  def post(self, request, *args, **kwargs):

    if request.method == "POST":
      comment_form = CommentForm(data = request.POST)
      if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.user = request.user
        new_comment.save()
      
    context = {
      "new_comment":new_comment
    }
    return render(request, "crud/news_comments.html", context)
  
class SearchListView(ListView):

  model = News
  template_name = 'search_results.html'
  context_object_name = 'barcha_yangiliklar'

  def get_queryset(self) -> QuerySet[Any]:
    query = self.request.GET.get("q")
    return News.objects.filter(
      Q(title__icontains = query) | Q(body__icontains = query)
    )