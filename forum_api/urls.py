from django.urls import path
from .views import *

app_name = 'forum_api'

urlpatterns = [
    path('', apiOverview,name='api-overview'),
    path('post-detail/<int:pk>/', PostDetails.as_view(),name='post-detail'),
    path('post-list/', PostList.as_view(),name='post-list'),
    path('post-create/', PostCreate.as_view(),name='post-create'),
    path('post-delete/<int:pk>/', PostDelete.as_view(),name='post-delete'),
    path('cat-detail/<int:pk>/', CategoryDetails.as_view(),name='category-detail'),
    path('cat-list/', CategoryList.as_view(),name='category-list'),
    path('cat-update/<int:pk>/', CategoryUpdate.as_view(),name='category-update'),
    path('cat-create/', CategoryCreate.as_view(),name='category-create'),
    path('cat-delete/<int:pk>/', CategoryDelete.as_view(),name='category-delete'),
    path('comment-detail/<int:pk>/', CommentDetails.as_view(),name='comment-detail'),
    path('comment-list/', CommentList.as_view(),name='comment-list'),
    path('comment-create/', CommentCreate.as_view(),name='comment-create'),
    path('comment-delete/<int:pk>/', CommentDelete.as_view(),name='comment-delete'),
    path('reply-detail/<int:pk>/', ReplyDetails.as_view(),name='reply-detail'),
    path('reply-list/', ReplyList.as_view(),name='reply-list'),
    path('reply-create/', ReplyCreate.as_view(),name='reply-create'),
    path('reply-delete/<int:pk>/', ReplyDelete.as_view(),name='reply-delete'),
]

# router = DefaultRouter()
# router.register('post',PostViewset,basename='post')
# router.register('cat',CategoryViewset,basename='cat')
# urlpatterns = [
#     path('', apiOverview,name='start'),
# ]

# urlpatterns += router.urls