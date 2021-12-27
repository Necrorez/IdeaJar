from django.db.models import fields
from rest_framework import serializers
from forum.models import Post, Category, Comment, Reply, PersonalMessage
from django.contrib.auth.models import User
from users.models import NewUser
class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('id','user_name','email','is_staff')
        read_only_fields = ('email', 'is_staff')
        write_only_fields = ('id',)
class PersonalMessageSerializer(serializers.ModelSerializer):
    author_email = serializers.CharField(source='sender.email',read_only=True)
    class Meta:
        model = PersonalMessage
        fields = ('id','sender','receiver','message','author_email')
        
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
        
class CommentSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        'posts_pk': 'post__pk'
    }
    user_email = serializers.CharField(source='user.email',read_only=True)
    user_role = serializers.CharField(source='user.is_staff',read_only=True)
    class Meta:
        model = Comment
        fields = ('id','user','comment','post','user_email','user_role')

class ReplySerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        'comment_pk': 'comment__pk',
    }
    user_email = serializers.CharField(source='user.email',read_only=True)
    user_role = serializers.CharField(source='user.is_staff',read_only=True)
    class Meta:
        model = Reply
        fields = ('id','user','reply','comment','user_email','user_role')



class PostSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        'category_pk': 'cat_pk',
    }
    author_email = serializers.CharField(source='author.email',read_only=True)
    author_role = serializers.CharField(source='author.is_staff',read_only=True)
    class Meta:
        model = Post
        read_only_fields = ('published',)
        fields = ('id','author','title','content','category','post_comment','published','author_email','author_role')

class CategorySerializer(serializers.ModelSerializer):
    post = PostSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ('id','name','description','post')

