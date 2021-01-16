from django.db import models
import datetime
from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField('Title name', max_length=200)
    article_text = models.TextField('Title text')
    pub_date = models.DateTimeField('publication date')

    def __str__(self):
    	return self.article_title

    def was_published_recently(self):
    	return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    def text_preveiw(self):
        return_text = self.article_text.split('.')[0]
        return return_text + ' ...'

class Comment(models.Model):
    parent_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField("Author's name", max_length=50)
    comment_text = models.CharField('Comment text', max_length=300)

    def __str__(self):
    	return self.author_name