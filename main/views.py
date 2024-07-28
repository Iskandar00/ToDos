from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ToDo
from .serializers import ToDoSerializer


class ToDoCreateListView(APIView):
    def post(self, request):
        serializer = ToDoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        to_dos_done = ToDo.objects.filter(done=True)
        to_dos_not_done = ToDo.objects.filter(done=False)
        all_to_dos = list(to_dos_done) + list(to_dos_not_done)
        serializer = ToDoSerializer(instance=all_to_dos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ToDoUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        to_dos = get_object_or_404(ToDo, pk=pk)
        serializer = ToDoSerializer(to_dos)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        to_dos = get_object_or_404(ToDo, pk=pk)
        serializer = ToDoSerializer(instance=to_dos, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        to_dos = get_object_or_404(ToDo, pk=pk)
        to_dos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
