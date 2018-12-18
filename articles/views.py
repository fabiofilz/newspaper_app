from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

# ARTICLES VIEW
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    template_name = 'article_new.html'
    fields = ['title', 'body'] # 'author' not visible
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class ArticleListView(LoginRequiredMixin, ListView):
    model = models.Article
    template_name = 'article_list.html'
    login_url = 'login'
    
class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = models.Article
    template_name = 'article_detail.html'
    login_url = 'login'
    
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Article
    fields = ['title', 'body', ]
    template_name = 'article_edit.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

# COMMENT VIEWS
class CommentDetailView(LoginRequiredMixin, DetailView):
    model = models.Comment
    template_name = 'comment_detail.html'
    login_url = 'login'
    
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Comment
    template_name = 'comment_delete.html'
    pk_url_kwarg = 'comment_pk'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Comment
    fields = ['comment']
    template_name = 'comment_edit.html'
    pk_url_kwarg = 'comment_pk'
    login_url = 'login'
    #success_url = reverse_lazy('article_list')

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('article_list')

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = models.Comment
    template_name = 'comment_new.html'
    fields = ['comment'] #, 'article']
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = get_object_or_404(models.Article, 
                                                  id=self.kwargs.get('article_pk'))
        return super().form_valid(form)
