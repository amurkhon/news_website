from django.urls import path
from .views import NewsListView, NewsListDetail,IndexView,contactPageView,Error_404,WorldNewsView,TechnologyNewsView,FinanceNewsView,SportNewsView

urlpatterns = [
  path('', IndexView.as_view(), name = 'home_page'),
  path('news/',NewsListView.as_view(),name = 'news_list_view'),
  path('news/<slug:slug>/',NewsListDetail.as_view(), name='news_detail'),
  path('contact-us/',contactPageView.as_view(), name='contact_page'),
  path('error-404/', Error_404, name='error_404'),
  path('jahon-yangiliklari/',WorldNewsView.as_view(), name='news_world'),
  path('fan-texnika-yangiliklari/',TechnologyNewsView.as_view(), name='news_technology'),
  path('iqtisodiyot-yangiliklari/',FinanceNewsView.as_view(), name='news_finance'),
  path('sport-yangiliklari/',SportNewsView.as_view(), name='news_sport')
]