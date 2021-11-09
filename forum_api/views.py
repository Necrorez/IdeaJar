
from rest_framework import generics,viewsets, status
from forum.models import Post,Category, Comment, Reply,PersonalMessage
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.permissions import SAFE_METHODS,BasePermission,IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class PostPermissions(BasePermission):
    message = 'Editing posts is restricted to the author and admin only'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_superuser

class CommentReplyPermissions(BasePermission):
    message = 'Editing posts is restricted to the author and admin only'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_superuser

class PrivateMessagePermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user or request.user.is_superuser or request.receiver == request.user

class CategoryPermissions(BasePermission):
    message = 'Editing posts is restricted to admins only'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff

class CategoryViewset(viewsets.ViewSet,CategoryPermissions):
    serializer_class=CategorySerializer
    permission_classes = [CategoryPermissions]
    def list(self, request,):
        queryset = Category.objects.filter()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.filter()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        queryset = Category.objects.get(pk=pk)
        serializer = CategorySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
 
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    def destroy(self, request,pk):
        queryset = Category.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    


class PostViewset(viewsets.ViewSet,PostPermissions):
    serializer_class = PostSerializer
    permission_classes = [PostPermissions]
    def list(self, request, category_pk=None):
        queryset = Post.objects.filter(category_id=category_pk)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, category_pk=None):
        queryset = Post.objects.filter(pk=pk,category_id=category_pk)
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request, category_pk=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def update(self, request, pk, category_pk=None):
        queryset = Post.objects.filter(pk=pk,category_id=category_pk)
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
 
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    def destroy(self, request,pk, category_pk=None):
        queryset = Post.objects.get(pk=pk,category_id=category_pk)
        queryset.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class CommentViewset(viewsets.ViewSet,CommentReplyPermissions):
    serializer_class=CommentSerializer
    permission_classes = [CommentReplyPermissions]
    def list(self, request,category_pk=None,posts_pk=None):
        queryset = Comment.objects.filter(post_id=posts_pk,post__category_id=category_pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None,category_pk=None,posts_pk=None):
        queryset = Comment.objects.filter()
        data = get_object_or_404(queryset, pk=pk,post__category_id=category_pk,post_id=posts_pk)
        serializer = CommentSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self, request,category_pk=None,posts_pk=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def update(self, request, pk,category_pk=None,posts_pk=None):
        queryset = Comment.objects.get(pk=pk,post__category_id=category_pk,post_id=posts_pk)
        serializer = CommentSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
 
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    def destroy(self, request,pk,category_pk=None,posts_pk=None):
        queryset = Comment.objects.get(pk=pk,post__category_id=category_pk,post_id=posts_pk)
        queryset.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser,IsAuthenticated]
        return [permission() for permission in permission_classes]

class ReplyViewset(viewsets.ViewSet,CommentReplyPermissions):
    serializer_class=ReplySerializer
    permission_classes = [CommentReplyPermissions]
    def list(self, request,category_pk=None,posts_pk=None,comments_pk=None):
        queryset = Reply.objects.filter(comment_id=comments_pk,comment__post_id=posts_pk,comment__post__category_id=category_pk)
        serializer = ReplySerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None,category_pk=None,posts_pk=None,comments_pk=None):
        queryset = Reply.objects.filter()
        data = get_object_or_404(queryset, pk=pk,comment_id=comments_pk)
        serializer = ReplySerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self, request,category_pk=None,posts_pk=None,comments_pk=None):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def update(self, request, pk,category_pk=None,posts_pk=None,comments_pk=None):
        queryset = Reply.objects.get(pk=pk,comment_id=comments_pk,comment__post_id=posts_pk,comment__post__category_id=category_pk)
        serializer = ReplySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
 
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    def destroy(self, request,pk,category_pk=None,posts_pk=None,comments_pk=None):
        queryset = Reply.objects.get(pk=pk,comment_id=comments_pk,comment__post_id=posts_pk,comment__post__category_id=category_pk)
        queryset.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser,IsAuthenticated]
        return [permission() for permission in permission_classes]

class PersonalMessageViewset(viewsets.ViewSet,PrivateMessagePermissions):
    serializer_class = PersonalMessageSerializer
    permission_classes = [PrivateMessagePermissions]

    def list(self, request,):
        queryset = PersonalMessage.objects.filter()
        serializer = PersonalMessageSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = PersonalMessage.objects.filter()
        data = get_object_or_404(queryset, pk=pk)
        serializer = PersonalMessageSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = PersonalMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        queryset = PersonalMessage.objects.get(pk=pk)
        serializer = PersonalMessageSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
 
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    def destroy(self, request,pk):
        queryset = PersonalMessage.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def apiOverview(request):
    
    api_urls = {
        'Category List':f'{request.build_absolute_uri()}categories/',
        'Category View':f'{request.build_absolute_uri()}categories/<int:pk>/',
        'Category Update':f'{request.build_absolute_uri()}categories/<int:pk>/',
        'Category Create':f'{request.build_absolute_uri()}categories/',
        'Category Delete':f'{request.build_absolute_uri()}categories/<int:pk>/',
        'Post List':f'{request.build_absolute_uri()}categories/<int:pk>/posts/',
        'Post View':f'{request.build_absolute_uri()}categories/<int:pk>/posts/<int:pk>/',
        'Post Create':f'{request.build_absolute_uri()}categories/<int:pk>/posts/',
        'Post Delete':f'{request.build_absolute_uri()}categories/<int:pk>/posts/<int:pk>/',
        'Comment List':f'{request.build_absolute_uri()}comment-list/',
        'Comment View':f'{request.build_absolute_uri()}comment-detail/<int:pk>/',
        'Comment Create':f'{request.build_absolute_uri()}comment-create/',
        'Comment Delete':f'{request.build_absolute_uri()}comment-delete/<int:pk>/',
        'Reply List':f'{request.build_absolute_uri()}reply-list/',
        'Reply View':f'{request.build_absolute_uri()}reply-detail/<int:pk>/',
        'Reply Create':f'{request.build_absolute_uri()}reply-create/',
        'Reply Delete':f'{request.build_absolute_uri()}reply-delete/<int:pk>/',
    }
    return Response(api_urls)

