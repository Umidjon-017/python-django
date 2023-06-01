from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateview, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit',BlogUpdateView.as_view(),name='post_edit'),
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateview.as_view(), name='post_new'),
]