from django.urls import path,include
from .views import *
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewset,basename='categories')

domainsRouter = routers.NestedSimpleRouter(router, r'categories', lookup='category')
domainsRouter.register(r'posts', PostViewset, basename='posts')

commentsRouter = routers.NestedSimpleRouter(domainsRouter,r'posts',lookup='posts')
commentsRouter.register(r'comments', CommentViewset, basename='comments')

replyRouter = routers.NestedSimpleRouter(commentsRouter,r'comments',lookup='comments')
replyRouter.register(r'replies',ReplyViewset,basename='replies')

personalMessageRouter = routers.DefaultRouter()
personalMessageRouter.register(r'personalMessage', PersonalMessageViewset,basename='personalMessage')
app_name = 'forum_api'

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(domainsRouter.urls)),
    path(r'', include(commentsRouter.urls)),
    path(r'', include(replyRouter.urls)),
    path(r'',include(personalMessageRouter.urls)),
    path('', apiOverview,name='api-overview'),
    
]

# router = DefaultRouter()
# router.register('post',PostViewset,basename='post')
# router.register('cat',CategoryViewset,basename='cat')
# urlpatterns = [
#     path('', apiOverview,name='start'),
# ]

# urlpatterns += router.urls
""" path('comment-detail/<int:pk>/', CommentDetails.as_view(),name='comment-detail'),
    path('comment-list/', CommentList.as_view(),name='comment-list'),
    path('comment-create/', CommentCreate.as_view(),name='comment-create'),
    path('comment-delete/<int:pk>/', CommentDelete.as_view(),name='comment-delete'),
    path('reply-detail/<int:pk>/', ReplyDetails.as_view(),name='reply-detail'),
    path('reply-list/', ReplyList.as_view(),name='reply-list'),
    path('reply-create/', ReplyCreate.as_view(),name='reply-create'),
    path('reply-delete/<int:pk>/', ReplyDelete.as_view(),name='reply-delete'), """