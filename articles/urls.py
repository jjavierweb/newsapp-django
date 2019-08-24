# import path
from django.urls import path

# import views
from .views import ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleCreateView

# create urlpatters
urlpatterns = [
  path('<int:pk>/edit/', ArticleUpdateView.as_view(), name = 'article_edit'),
  path('<int:pk>/', ArticleDetailView.as_view(), name = 'article_detail'),
  path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
  path('create/', ArticleCreateView.as_view(), name = 'article_create'),
  path('', ArticleListView.as_view(), name='article_home'),

]