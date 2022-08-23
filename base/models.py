from django.db import models

# Create your models here.
class Topics(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)

class User(models.Model):
    email=models.EmailField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    def __str__(self):
        return str(self.username)

class Room(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    topic=models.ForeignKey(Topics, on_delete=models.CASCADE)
    host=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)

class Message(models.Model):
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    body=models.TextField()
    posted=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.body)

class Question(models.Model):
    question=models.TextField()
    topic=models.ForeignKey(Topics, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    posted=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.question)

class Answer(models.Model):
    answer=models.TextField()
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    posted=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.answer)

class Follows(models.Model):
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user,"-",self.room)
