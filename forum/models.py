from django.db import models
from users.models import NewUser as User
import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='forum_post')
    title = models.CharField(max_length=100)
    content = models.TextField(null=False)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=1,related_name='post')
    published = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=250,unique_for_date='published')
    objects = models.Manager()

    class Meta:
        ordering = ('-published',)

    def __str__(self) -> str:
        return f"{self.author} {self.title}" 
    
class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post,null=True,on_delete=models.CASCADE,related_name='post_comment')
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user} {self.post}"

class Reply(models.Model):
    reply = models.TextField()
    comment = models.ForeignKey(Comment,null=True,on_delete=models.CASCADE,related_name='comment_rep')
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user} {self.comment}"

class PersonalMessage(models.Model):
    sender = models.ForeignKey(User,null=False,on_delete=models.CASCADE,related_name='sender')
    receiver = models.ForeignKey(User,null=False ,on_delete=models.CASCADE,related_name='receiver') 
    message = models.TextField()
    def __str__(self):
        return f"{self.sender} { self.message} {self.message}"
    