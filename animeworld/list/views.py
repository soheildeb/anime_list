from django.shortcuts import render
from django.template import loader
from .models import Anime
from django.http import HttpResponse

def index(request):
        template = loader.get_template('index.html')
        anime_list = Anime.objects.all().values()
        context = {
                'list':anime_list,
        }

        return HttpResponse(template.render(context,request))