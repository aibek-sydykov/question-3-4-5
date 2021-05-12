from django.contrib import admin
from django.urls import path
from post.views import PostView, CommentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostView.as_view({'get': 'list', 'post': 'create'})),
    path('post/<int:pk>', PostView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('comment', CommentView.as_view({'post': 'create'})),
    path('comment/<int:pk>', CommentView.as_view({'put': 'update', 'delete': 'destroy'})),
]
