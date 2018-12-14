from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', views.ArticleCreateView.as_view(), name='article_new'),

    path('<article_pk>/comment/<comment_pk>', views.CommentDetailView.as_view(), name='comment_detail'),
    url(r'^(?P<pk>\d+)/comment/(?P<comment_pk>\d+)/delete/$', views.CommentDeleteView.as_view(), name='comment_delete'),
    url(r'^(?P<pk>\d+)/comment/(?P<comment_pk>\d+)/edit/$', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('<article_pk>/comment/new/', views.CommentCreateView.as_view(), name='comment_new'),
]
