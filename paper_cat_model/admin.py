from django.contrib import admin
from .models import Author, Keyword, Category, Academy, Paper, KeywordRelationship, AuthorRelationship, CategoryRelationship

admin.site.register(Author)
admin.site.register(Keyword)
admin.site.register(Category)
admin.site.register(Academy)
admin.site.register(Paper)
admin.site.register(KeywordRelationship)
admin.site.register(AuthorRelationship)
admin.site.register(CategoryRelationship)




