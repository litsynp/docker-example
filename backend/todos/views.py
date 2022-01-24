from rest_framework import viewsets

from todos.serializers import TodoSerializer
from todos.models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
