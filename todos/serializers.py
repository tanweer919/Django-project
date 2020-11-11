from rest_framework import serializers
from todos.models import Todo, TodoImage


class TodoImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(method_name='get_image_url')

    def get_image_url(self, todoImage):
        if todoImage.image:
            return todoImage.image.url
        else:
            return None

    class Meta:
        model = TodoImage
        fields = ("id", "image_url")


class TodoSerializer(serializers.ModelSerializer):

    todo_images = TodoImageSerializer(source="todo_image", many=True)
    class Meta:
        model = Todo
        read_only_fields = ("id", "createdAt", "updatedAt")
        fields = ("id", "title", "description", "completed", "createdAt", "updatedAt", "todo_images")


