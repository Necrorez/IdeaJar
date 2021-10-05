
from rest_framework import generics,viewsets
from forum.models import Post,Category, Comment, Reply
from .serializers import CategorySerializer, PostSerializer, CommentSerializer, ReplySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
# Create your views here.

#Testing
class CategoryViewset(viewsets.ViewSet):
    serializer_class=CategorySerializer
    def list(self, request,):
        queryset = Category.objects.filter()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.filter()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

    def update(self, request, pk):
        queryset = Category.objects.get(pk=pk)
        serializer = CategorySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
 
        return Response(serializer.data)

    def destroy(self, request,pk):
        queryset = Category.objects.get(pk=pk)
        queryset.delete()

class PostViewset(viewsets.ViewSet):
    serializer_class = PostSerializer

    def list(self, request, category_pk=None):
        queryset = Post.objects.filter(category_id=category_pk)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, category_pk=None):
        queryset = Post.objects.filter(pk=pk,category_id=category_pk)
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def create(self, request, category_pk=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def update(self, request, pk, category_pk=None):
        queryset = Post.objects.filter(pk=pk,category_id=category_pk)
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
 
        return Response(serializer.data)

    def destroy(self, request,pk, category_pk=None):
        queryset = Post.objects.get(pk=pk,category_id=category_pk)
        queryset.delete()



#Comment logic
class CommentDetails(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDelete(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Reply logic
class ReplyDetails(generics.RetrieveAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class ReplyList(generics.ListAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class ReplyCreate(generics.CreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


class ReplyDelete(generics.DestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
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

