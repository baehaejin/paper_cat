from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)


class Keyword(models.Model):
    keyword = models.CharField(max_length=100)


class Category(models.Model):
    category = models.CharField(max_length=100)


class Academy(models.Model):
    academy = models.TextField()
    priority = models.IntegerField(null=True, default=0)

    def get_priority(self, priority):
        self.priority = priority


class Paper(models.Model):
    title = models.TextField()
    citation = models.IntegerField(null=True, default=0)
    href = models.TextField()
    abstraction = models.TextField()
    priority = models.IntegerField(null=True, default=0)
    author = models.ManyToManyField(Author)
    keyword = models.ManyToManyField(Keyword)
    academy = models.ManyToManyField(Academy)

    def set_priority(self, priority):
        self.priority = priority


class KeywordRelationship(models.Model):
    keyword = models.ManyToManyField(Keyword)
    paper = models.OneToOneField(Paper, on_delete=models.CASCADE)


class AuthorRelationship(models.Model):
    author = models.ManyToManyField(Author)
    paper = models.OneToOneField(Paper, on_delete=models.CASCADE)


class CategoryRelationship(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    paper = models.OneToOneField(Paper, on_delete=models.CASCADE)

