
from rest_framework import generics
from forum.models import Post,Category, Comment, Reply
from .serializers import CategorySerializer, PostSerializer, CommentSerializer, ReplySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# Post logic
class PostDetails(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

#Category logic
class CategoryDetails(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDelete(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdate(generics.UpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

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
        'Category List':f'{request.build_absolute_uri()}cat-list/',
        'Category View':f'{request.build_absolute_uri()}cat-detail/<int:pk>/',
        'Category Update':f'{request.build_absolute_uri()}cat-update/<int:pk>/',
        'Category Create':f'{request.build_absolute_uri()}cat-create/',
        'Category Delete':f'{request.build_absolute_uri()}cat-delete/<int:pk>/',
        'Post List':f'{request.build_absolute_uri()}post-list/',
        'Post View':f'{request.build_absolute_uri()}post-detail/<int:pk>/',
        'Post Create':f'{request.build_absolute_uri()}post-create/',
        'Post Delete':f'{request.build_absolute_uri()}post-delete/<int:pk>/',
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

# class PostViewset(viewsets.ViewSet):
#     queryset = Post.objects.all()
#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset,many=True)
#         return Response(serializer_class.data)
#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset,pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)
#     def create(self, request):
#         pass
#     def destroy(self, request, pk=None):
#         pass

# class CategoryViewset(viewsets.ViewSet):
#     queryset = Category.objects.all()
#     def list(self, request):
#         serializer_class = CategorySerializer(self.queryset,many=True)
#         return Response(serializer_class.data)
#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset,pk=pk)
#         serializer_class = CategorySerializer(post)
#         return Response(serializer_class.data)
#     def create(self, request):
#         pass
#     def destroy(self, request, pk=None):
#         pass