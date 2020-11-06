from rest_framework.serializers import ModelSerializer
from todos.models import Todo

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        read_only_fields = ("id", "createdAt", "updatedAt")
        fields = ("id", "title", "description", "completed", "createdAt", "updatedAt")