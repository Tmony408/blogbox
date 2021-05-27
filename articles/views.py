from django.shortcuts import get_object_or_404, render,redirect
from .models import Article
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from comments.models import Comment
from django.contrib import messages

# Create your views here.
def articles(request):
    
    articles= Article.objects.order_by('-post_date').filter(is_published = True)
    latestarticles= Article.objects.order_by('-post_date').filter(is_published = True)[:2]
    paginator = Paginator(articles,12 )
    page= request.GET.get('page')
    paged_articles= paginator.get_page(page)

    textcontent = {
        'articles' : paged_articles,
        'latestarticles' : latestarticles,
    }
    return render(request,'articles.html', textcontent)




def article(request, article_id):

    article= get_object_or_404(Article, pk = article_id)
    comments= Comment.objects.order_by('-comment_date').filter(article_id=article_id)
    latestarticles= Article.objects.order_by('-post_date').filter(is_published = True)[:2]
    recentarticles= Article.objects.order_by('-post_date').filter(is_published = True)[:5]
    comments_no = comments.count()
    textcontent = {
        'article' : article,
        'latestarticles' : latestarticles,
        'recents': recentarticles,
        'comments' : comments,
        'comments_no': comments_no
    }
    return render(request,'article.html', textcontent)


def comment(request):
    if request.method== 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone=request.POST['phone']
        articles_id= request.POST['articles_id']
        message = request.POST['message']
        

        comment = Comment(name=name, email=email, message=message,phone=phone, article_id=articles_id)
        comment.save()
        # send_mail(
        #     subject,
        #     messages,
        #     EMAIL_HOST_USER,
        #     ['adetulatestimony@gmail.com'],
        #     fail_silently=False,
        # ) 
        # messages.success(request, 'Thanks for comenting on our post')
        return redirect('/articles/'+articles_id)
    return redirect('/articles/'+articles_id)
def search(request):
    article_id= request.GET['article_id']
    
    if 'keywords' in request.GET: 
        keywords= request.GET['keywords']
        if keywords:
            articles= Article.objects.order_by('-post_date').filter(is_published = True, description__icontains=keywords)
            latestarticles= Article.objects.order_by('-post_date').filter(is_published = True)[:2]
            header= keywords
            textcontent = {
                'articles' : articles,
                'latestarticles' : latestarticles,
                'header' : header
            }
            return render(request,'articles.html', textcontent)
    else:
        return redirect('/articles/'+article_id)  
    
def international(request):
    articles= Article.objects.order_by('-post_date').filter(is_published = True, title__iexact='international')
    latestarticles= Article.objects.order_by('-post_date').filter(is_published = True)[:2]
    paginator = Paginator(articles,12 )
    page= request.GET.get('page')
    paged_articles= paginator.get_page(page)
    header= 'International News'

    textcontent = {
        'articles' : paged_articles,
        'latestarticles' : latestarticles,
        'header' : header
    }
    return render(request,'articles.html', textcontent)
def sport(request):
    articles= Article.objects.order_by('-post_date').filter(is_published = True, title__iexact='sport')
    latestarticles= Article.objects.order_by('post_date').filter(is_published = True)[:2]
    paginator = Paginator(articles,12 )
    page= request.GET.get('page')
    paged_articles= paginator.get_page(page)
    header = 'Sports News'
    textcontent = {
        'articles' : paged_articles,
        'latestarticles' : latestarticles,
        'header' : header,
    }
    return render(request,'articles.html', textcontent)
def entertainment(request):
    articles= Article.objects.order_by('-post_date').filter(is_published = True, title__iexact='entertainment')
    latestarticles= Article.objects.order_by('-post_date').filter(is_published = True)[:2]
    paginator = Paginator(articles,12 )
    page= request.GET.get('page')
    paged_articles= paginator.get_page(page)
    header = 'Entertainment News'

    textcontent = {
        'articles' : paged_articles,
        'latestarticles' : latestarticles,
        'header' : header,
    }
    return render(request,'articles.html', textcontent)
def local(request):
    articles= Article.objects.order_by('-post_date').filter(is_published = True, title__iexact='local')
    latestarticles= Article.objects.order_by('-post_date').filter(is_published = True)[:2]
    paginator = Paginator(articles,12 )
    page= request.GET.get('page')
    paged_articles= paginator.get_page(page)
    header = 'Local News'

    textcontent = {
        'articles' : paged_articles,
        'latestarticles' : latestarticles,
        'header' : header,
    }
    return render(request,'articles.html', textcontent)
def education(request):
    articles= Article.objects.order_by('-post_date').filter(is_published = True, title__iexact= 'education')
    latestarticles= Article.objects.order_by('-post_date').filter(is_published = True)[:2]
    paginator = Paginator(articles,12 )
    page= request.GET.get('page')
    paged_articles= paginator.get_page(page)
    header = 'Education News'

    textcontent = {
        'articles' : paged_articles,
        'latestarticles' : latestarticles,
        'header' : header
    }
    return render(request,'articles.html', textcontent)