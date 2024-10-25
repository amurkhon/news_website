from django.urls import path
from .views import CommentsView,NewsDetailView,IndexView, SearchListView,contactPageView,Error_404,WorldNewsView,TechnologyNewsView,FinanceNewsView,SportNewsView,UpdateNewsView,DeleteNewsView,CreateNews

urlpatterns = [
  path('', IndexView.as_view(), name = 'home_page'),
  path('news/<int:pk>/',NewsDetailView.as_view(), name='news_detail_page'),
  path('news/<slug:slug>/delete/', DeleteNewsView.as_view(), name='news_delete'),
  path('news/<slug:slug>/edit/', UpdateNewsView.as_view(), name='news_edit'),
  path('create/', CreateNews.as_view(), name='news_create'),
  path('contact-us/',contactPageView.as_view(), name='contact_page'),
  path('error-404/', Error_404, name='error_404'),
  path('jahon-yangiliklari/',WorldNewsView.as_view(), name='news_world'),
  path('fan-texnika-yangiliklari/',TechnologyNewsView.as_view(), name='news_technology'),
  path('iqtisodiyot-yangiliklari/',FinanceNewsView.as_view(), name='news_finance'),
  path('sport-yangiliklari/',SportNewsView.as_view(), name='news_sport'),
  path('comments/', CommentsView.as_view(), name = 'news_comment'),
  path('search/', SearchListView.as_view(), name='search_results'),
]