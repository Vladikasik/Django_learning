from django.db import models


class Article(models.Model):
    article_title = models.CharField('Title name', max_length=200)
    article_text = models.TextField('Title text')
    pub_date = models.DateTimeField('publication date')

    def __str__(self):
    	return self.article_title


class Comment(models.Model):
    parent_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField("Author's name", max_length=50)
    comment_text = models.CharField('Comment text', max_length=300)

    def __str__(self):
    	return self.author_name