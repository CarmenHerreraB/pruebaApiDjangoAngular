from rest_framework import viewsets  # importante para generar los endpoints automaticamente - Necesario para usar ModelViewSet
from rest_framework.response import Response  #Necesario para devolver respuestas HTTP personalizadas.
from rest_framework import status #Necesario para devolver códigos de estado HTTP (201, 400, 404, etc.).
from .models import Student # Necesario para consultar el modelo Student.
from .serializers import StudentSerializer #  Necesario para convertir los datos de Python a JSON y viceversa.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Added Successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to Add"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            student = self.get_object()
            serializer = self.get_serializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Updated Successfully"}, status=status.HTTP_200_OK)
            return Response({"message": "Failed to Update"}, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({"message": "Student Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            student = self.get_object()
            student.delete()
            return Response({"message": "Deleted Successfully"}, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"message": "Student Not Found"}, status=status.HTTP_404_NOT_FOUND)
