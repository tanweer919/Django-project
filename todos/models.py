from django.db import models


class Todo(models.Model):

    title:str = models.CharField(max_length=100)
    description:str = models.CharField(max_length=200, null=True, blank=True)
    completed = models.PositiveIntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class TodoImage(models.Model):
    todo = models.ForeignKey(Todo, related_name="todo_image", on_delete=models.PROTECT)
    image = models.FileField(upload_to='image')

