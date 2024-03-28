from django.db import models

class Review(models.Model):
    user_id = models.IntegerField()
    event_id = models.IntegerField()
    registration_experience = models.IntegerField()
    event_experience = models.IntegerField()
    breakfast_experience = models.IntegerField()
    overall_experience = models.IntegerField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class FlaggedReview(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    report_count = models.IntegerField(default=0)