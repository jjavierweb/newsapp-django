from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.TabularInline):
  model =Comment

class AticleAdmin(admin.ModelAdmin):
  inlines = [ CommentInline, ]

# Register your models here.
admin.site.register(Article, AticleAdmin)
admin.site.register(Comment)
