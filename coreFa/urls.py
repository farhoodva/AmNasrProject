from django.urls import path
from .views import *
app_name = 'coreFa'


urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('', HomeView.as_view(), name='home'),
    path('news-and-articles', NewsListView.as_view(), name='article-list-view'),
    path('news-and-articles/<pk>', NewsDetailView.as_view(), name='article-detail-view'),
    path('galley', GalleryListView.as_view(), name='gallery'),
    path('plans', PlansListView.as_view(), name='plans'),
    path('our-projects', ProjectsView.as_view(), name='our-projects'),
    path('about-haatam-central-baazar', AboutUsView.as_view(), name='about-us'),
    ]