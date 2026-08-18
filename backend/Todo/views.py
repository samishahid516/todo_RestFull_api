from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import todo_serilizer


class todo_list(APIView):

    def get(self, request):
        todos = Todo.objects.all()
        serializer = todo_serilizer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = todo_serilizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class todo_detail(APIView):

    def get(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        serializer = todo_serilizer(todo)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        serializer = todo_serilizer(todo,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        serializer = todo_serilizer(todo,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)