from django.shortcuts import render, get_object_or_404

from django.views import generic

from coreFa.models import *


class HomeView(generic.View):
    def get(self, request):
        news = NewsAndArticles.objects.all().order_by('created_at').filter(active=True)[:4]
        return render(self.request, 'home.html', context={'news': news})


class NewsListView(generic.ListView):
    model = NewsAndArticles
    template_name = 'new-list-view.html'

    def get_queryset(self):
        return NewsAndArticles.objects.all().order_by('created_at')


class NewsDetailView(generic.DetailView):
    model = NewsAndArticles
    template_name = 'news-detail.view.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_items'] = NewsAndArticles.objects.all().order_by('created_at').filter(active=True)[:4]
        return context

    def get_object(self, queryset=None):
        news = get_object_or_404(NewsAndArticles, pk=self.kwargs['pk'])
        return news


class GalleryListView(generic.ListView):
    model = GalleryImages
    template_name = 'gallery.html'
    paginate_by = 8

    def get_queryset(self):
        return GalleryImages.objects.all().order_by('-pk')


class PlansListView(generic.ListView):
    model = Plans
    template_name = 'plans.html'
    paginate_by = 8

    def get_queryset(self):
        return Plans.objects.all().order_by('-pk')