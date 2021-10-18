from django.db import models
import sys
from account.models import Account

class Todo(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    title:str = models.CharField(max_length=101)
    description:str = models.CharField(max_length=201, null=True, blank=True)
    completed = models.PositiveIntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.id:
            old_todo = Todo.objects.get(id=self.id)
            if self.completed == 1 and old_todo.completed == 0:
                print("completed", file=sys.stderr)
        super().save(force_insert, force_update, using, update_fields)


class TodoImage(models.Model):
    todo = models.ForeignKey(Todo, related_name="todo_image", on_delete=models.PROTECT)
    image = models.FileField(upload_to='image')

