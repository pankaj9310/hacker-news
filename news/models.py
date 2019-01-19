from django.db import models
# Create your models here.
class News(models.Model):
    username = models.CharField(max_length=128)
    title    = models.CharField(max_length=256)
    url      = models.CharField(max_length=256)
    upvote   = models.IntegerField()
    description = models.TextField()
    sentiment_score = models.FloatField()
    story_type = models.CharField(max_length=64)
    hacker_news_id = models.IntegerField()
    posted_at = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username