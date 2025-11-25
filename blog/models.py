from django.db import models
from django.contrib.auth.models import User

STATUS = ((0,"Draft"), (1,"Published"))

# Create your models here.
class Event_Post(models.Model):
    event_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "event_post")
    title = models.CharField(max_length=200)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    slug = models.SlugField(max_length = 200, unique = True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices= STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(Event_Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "comment_author")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)


    