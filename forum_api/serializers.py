from django.db.models import fields
from rest_framework import serializers
from forum.models import Post, Category, Comment, Reply



class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('id','user','reply','comment')

class CommentSerializer(serializers.ModelSerializer):
    comment_rep = ReplySerializer(many=True,read_only=True)
    class Meta:
        model = Comment
        fields = ('id','user','comment','comment_rep','post')

class PostSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        'category_pk': 'cat_pk',
    }
    post_comment = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ('id','auther','title','content','category','post_comment')

class CategorySerializer(serializers.ModelSerializer):
    post = PostSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ('id','name','description','post')

