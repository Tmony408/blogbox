from django.shortcuts import render
from articles.models import Article

# Create your views here.
def home(request):
    articles= Article.objects.order_by('-post_date').filter(is_published = True)[:9] 
    latestarticles= Article.objects.order_by('post_date').filter(is_published = True)[:2]
    homeContent={
        'articles': articles,
        'latestarticles' : latestarticles,
    }
    return render(request,'home.html', homeContent)