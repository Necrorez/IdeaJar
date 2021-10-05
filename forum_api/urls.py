from django.urls import path,include
from .views import *
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r'categories', CategoryViewset,basename='categories')

domains_router = routers.NestedSimpleRouter(router, r'categories', lookup='category')
domains_router.register(r'posts', PostViewset, basename='posts')

app_name = 'forum_api'

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(domains_router.urls)),
    path('', apiOverview,name='api-overview'),
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