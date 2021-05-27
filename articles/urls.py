"""tmonyblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
   path('',views.articles,name='articles'),
   path('<int:article_id>',views.article,name='article'),
   path('search',views.search,name='search'),
   path('education',views.education,name='education'),
   path('entertainment',views.entertainment,name='entertainment'),
   path('local',views.local,name='local'),
   path('international',views.international,name='international'),
   path('sport',views.sport,name='sport'),
   path('comment',views.comment,name='comment')
   
]
