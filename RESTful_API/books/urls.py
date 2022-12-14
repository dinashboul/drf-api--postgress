from django.urls import path
from .views import BookListView,BookDetailView,PostListView,PostDetailView
urlpatterns = [
   path('', BookListView.as_view(), name='Book_list'),
   path('<int:pk>', BookDetailView.as_view(),name='Book_detail'),
    path('posts/', PostListView.as_view(), name='post_list'),
   path('posts/<int:pk>', PostDetailView.as_view(),name='post_detail')
]
