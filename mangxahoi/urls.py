from django.urls import path

#from . import views
from .views import MangxahoiView, ChitietView, AddPostView, UpdatePostView, DeletePostView, LikeView, AddCommentView, CommentLikeView, UpdateCommentView, DeleteCommentView


app_name = 'mangxahoi'
urlpatterns = [
    #path('', views.mangxahoi, name='mangxahoi'),
    path('', MangxahoiView.as_view(), name='mangxahoi'),
    path('chitiet/<int:pk>/', ChitietView.as_view(), name='chitiet'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('update_post/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('chitiet/<int:pk>/delete_post/', DeletePostView.as_view(), name='delete_post'),

    path('like/<int:pk>', LikeView, name='like_post'),

    path('chitiet/<int:pk>/add_comment', AddCommentView.as_view(), name='add_comment'),
    path('chitiet/update_comment/<int:pk>/', UpdateCommentView.as_view(), name='update_comment'),
    path('chitiet/<int:pk>/delete_comment/', DeleteCommentView.as_view(), name='delete_comment'),
    path('commentlike/<int:pk>', CommentLikeView, name='like_comment'),
]