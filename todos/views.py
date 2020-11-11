from rest_framework import generics, views, status
from todos.models import Todo
from todos.serializers import TodoSerializer
from rest_framework.response import Response
from  rest_framework.permissions import AllowAny

class TodosRetrieveView(generics.ListAPIView):

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class CreateTodoView(generics.CreateAPIView):

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()




class TodoRetrieveView(generics.RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    lookup_field = 'id'


class CompleteTodoView(views.APIView):

    def post(self, request):
        id = request.data.get('id', None)
        todo = Todo.objects.get(id=id)
        todo.completed = 1
        todo.save()
        return Response({'success': True}, status=status.HTTP_200_OK)





