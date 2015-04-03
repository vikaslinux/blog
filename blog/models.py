from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

# Create your models here.
class bloguser(models.Model):
    user=models.OneToOneField(User)
    profile_pic=models.ImageField(upload_to="pics")
    dob=models.DateField()
    def __str__(self):
        return self.user.first_name
class Post(models.Model):
    post_title=models.CharField(max_length=1000)
    post_text=models.CharField(max_length=1000)
    datetime=models.DateTimeField(auto_now_add=True)
    postuser=models.ForeignKey(User,null=True)
    def __str__(self):
        return self.post_title
class Comment(models.Model):
    post=models.ForeignKey(Post)
    comment_text=models.CharField(max_length=140)
    comment_datetime=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_text