from rest_framework import generics
from todos.models import Todo
from todos.serializers import TodoSerializer

class TodoRetrieveView(generics.ListAPIView):

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
