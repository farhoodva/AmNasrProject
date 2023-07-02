from django.shortcuts import render ,get_object_or_404

from django.views import generic

from coreFa.models import *


class HomeView(generic.View):
    def get(self, request):
        news = NewsAndArticles.objects.all()
        return render(self.request, 'home.html', context={'news':news})