from django.shortcuts import render
from home.models import Home
from clients.models import Client
from articles.models import Article

# Create your views here.
def team(request):
    video= Home.objects.order_by('-create_date')[:1]
    clients= Client.objects.order_by('testimonial_date')
    latestarticles= Article.objects.order_by('-post_date').filter(is_published = True)[:2]
    
    content={
        'videos': video,
        'clients': clients,
        'latestarticles' : latestarticles,

    }

    return render(request,'team.html', content)
def video(request):
    return render(request,'video.html',)