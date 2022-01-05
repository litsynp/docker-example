from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets

from todos.serializers import TodoSerializer
from todos.models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


# Create your views here.

# @api_view(['POST', ])
# def create(request):
#     index = Todolist.objects.create(
#         contents=request.data['contents'],
#         title=request.data['title']
#     )
#     index.save()
#     return Response("delete posting", status=status.HTTP_200_OK)


# @api_view(['GET', ])
# def read(request):
#     index = Todolist.objects.create(
#         contents=request.data['contents'],
#         title=request.data['title']
#     )
#     index.save()
#     return Response("delete posting", status=status.HTTP_200_OK)


# @api_view(['PUT', ])
# def update(request):
#     index = Todolist.objects.create(
#         contents=request.data['contents'],
#         title=request.data['title']
#     )
#     index.save()
#     return Response("delete posting", status=status.HTTP_200_OK)


# @api_view(['DELETE', ])
# def delete(request):
#     index = Todolist.objects.create(
#         contents=request.data['contents'],
#         title=request.data['title']
#     )
#     index.save()
#     return Response("delete posting", status=status.HTTP_200_OK)
