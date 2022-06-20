from django.shortcuts import render
from django.template import loader
from .models import Anime
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect

def index(request):
        template = loader.get_template('index.html')
        anime_list = Anime.objects.all().values()
        context = {
                'list':anime_list,
        }

        return HttpResponse(template.render(context,request))

def add(request):
        template = loader.get_template('add.html')
        return HttpResponse(template.render({},request))

def addrecord(request):
        x = request.POST['description']
        y = request.POST['description']
        z = request.POST['episodes']
        anime = Anime(
                name=x,
                description=y,
                episodes=z,
        )
        anime.save()
        return HttpResponseRedirect(reverse('index'))

def delete(request,id):
        anime = Anime.objects.get(id=id)
        anime.delete()
        return HttpResponseRedirect(reverse("index"))

def update (request,id):
        anime = Anime.objects.get(id=id)
        template = loader.get_template('update.html')
        context = {
                "anime":anime
        }
        return HttpResponse(template.render(context,request))

def updaterecord (request,id):
        x = request.POST["new_name"]
        y = request.POST["new_description"]
        z = request.POST["new_episodes"]
        anime = Anime.objects.get(id=id)
        anime.name = x
        anime.description = y
        anime.episodes = z
        anime.save()
        return HttpResponseRedirect(reverse("index"))

