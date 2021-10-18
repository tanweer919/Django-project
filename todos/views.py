from rest_framework import generics, views, status, parsers
from todos.models import Todo, TodoImage
from todos.serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import permissions

class TodoAccessPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.account == request.user

class TodosRetrieveView(generics.ListAPIView):

    serializer_class = TodoSerializer
    def get_queryset(self):
        return Todo.objects.filter(account=self.request.user)


class CreateTodoView(generics.CreateAPIView):

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()




class TodoRetrieveView(generics.RetrieveAPIView):

    permission_classes = (TodoAccessPermission,)
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    lookup_field = 'id'


class TodoTitleRetrieveView(views.APIView):
    permission_classes = (TodoAccessPermission,)

    def get(self, request):
        title = request.kwargs['title']
        todo = Todo.objects.filter(title=title)
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompleteTodoView(views.APIView):
    permission_classes = (TodoAccessPermission,)

    def post(self, request):
        id = request.data.get('id', None)
        todo = Todo.objects.get(id=id)
        todo.completed = 1
        todo.save()
        return Response({'success': True}, status=status.HTTP_200_OK)


class AddTodoImageView(views.APIView):
    parser_classes = (parsers.MultiPartParser,)

    def post(self, request):
        todo_id = request.data.get("todo_id", None)
        image = request.data.get("image", None)
        try:
            todo = Todo.objects.get(id=todo_id)
            TodoImage.objects.create(todo=todo, image=image)
            return Response({"success": True}, status=status.HTTP_201_CREATED)
        except Todo.DoesNotExist:
            return Response({"success": False}, status=status.HTTP_404_NOT_FOUND)






