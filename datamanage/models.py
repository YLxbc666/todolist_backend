from django.db import models


# Create your models here.
class QuestionsModel(models.Model):
    uuid = models.CharField(max_length=200)
    question = models.TextField()
    answer = models.CharField(max_length=200)
    options = models.JSONField(default=list)

    def __str__(self):
        return self.question
