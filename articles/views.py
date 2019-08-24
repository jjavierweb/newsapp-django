from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

# import the LoginRequiredMixin for authorization
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# import the model
from .models import Article


# Create your views here.
# create class view for the list of articles
class ArticleListView(LoginRequiredMixin,ListView):
  model = Article
  template_name = 'articles/articles_home.html'
  context_object_name = 'articles_list'
  login_url = 'login'

class ArticleDetailView(LoginRequiredMixin,DetailView):
  model = Article
  template_name='articles/articles_detail.html'
  login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Article
  fields = ('title', 'body')
  template_name = 'articles/articles_edit.html'
  login_url= 'login'

  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user
  

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Article
  template_name = 'articles/articles_delete.html'
  success_url = reverse_lazy('article_home')
  login_url='login'

  # define method to check that user logged in is the same as author an allow delete
  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin,CreateView):
  model = Article
  template_name = 'articles/articles_create.html'
  fields = ('title','body')
  login_url='login'

  # define method to add the author to the form
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
