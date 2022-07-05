from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=50)  
    number_of_questions = models.IntegerField(default=1)
    time = models.IntegerField(default="1")   
    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    giaidap = models.TextField()
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.BooleanField(default=False)
    def __str__(self):
        return self.choice_text
    
