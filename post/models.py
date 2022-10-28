from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Post(models.Model):
    author          = models.ForeignKey(User , on_delete = models.CASCADE)
    title           = models.CharField(blank = False , null = False , max_length = 200)
    content         = models.TextField(max_length = 500)
    created_at      = models.DateTimeField(auto_now_add = True)
    activity        = GenericRelation("post.Activity")
    
    def __str__(self):
        return str(self.title)
    
    @property
    def get_model_type(self):
        return "Post"
    
class Comment(models.Model):
    commenter               = models.ForeignKey(User , on_delete = models.CASCADE)
    comment                 = models.TextField(max_length = 100)
    commented_at            = models.DateTimeField(auto_now_add = True)
    activity                = GenericRelation("post.Activity")
        
    @property
    def get_model_type(self):
        return "Comment"
    
    def __str__(self):
        return self.commenter.username + " commented " + self.comment[:20] + " ."
    
class Activity(models.Model):
    class ActivityType(models.TextChoices):
        LIKE    = "LIKE" , "like"
        DISLIKE = "DISLIKE" , "dislike"
    activity                = models.CharField(max_length = 7 , choices = ActivityType.choices)
    user                    = models.ForeignKey(User , on_delete = models.CASCADE)
    done_at                 = models.DateTimeField(auto_now_add = True)
    
    content_type            = models.ForeignKey(ContentType , on_delete = models.CASCADE)
    object_id               = models.PositiveIntegerField()
    content_object          = GenericForeignKey()
    
    def __str__(self):
            return self.user.username +  " : " + self.activity + " : " + str(self.content_object.get_model_type)
        





