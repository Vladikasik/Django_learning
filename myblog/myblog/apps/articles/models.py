from django.db import models


class Article(models.Model):
    article_title = models.CharField('Title name', max_length=200)
    article_text = models.TextField('Title text')
    article_author = models.CharField('Author Name')
    pub_date = models.DateTimeField('publication date')



class Comment(models.Model):
    pass
