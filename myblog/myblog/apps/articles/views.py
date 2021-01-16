from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article, Comment

def index(request):
	latest_articles_list = Article.objects.order_by('-pub_date')[:5]
	return render(request, 'articles/list.html', {"articles_list": latest_articles_list})


def detail(request, article_id):
	try:
		article = Article.objects.get( id = article_id )
	except:
		raise Http404("Статья не найдена )= ")

	return render(request, 'articles/detail.html', {'article': article})

def leave_comment(request, article_id):
	pass