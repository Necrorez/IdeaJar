from django.db.models import fields
from rest_framework import serializers
from forum.models import Post, Category, Comment, Reply, PersonalMessage
from django.contrib.auth.models import User
 
class PersonalMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalMessage
        fields = ('id','sender', 'receiver', 'message')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
class ReplySerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        'category_pk': 'cat_pk',
        'posts_pk': 'post__pk',
        'comment_pk': 'comment__pk',
    }
    class Meta:
        model = Reply
        fields = ('id','user','reply','comment')

class CommentSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        'posts_pk': 'post__pk'
    }
    class Meta:
        model = Comment
        fields = ('id','user','comment','post')

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

