from rest_framework import viewsets
from freshot.models import Student
from freshot.serializer import StudentSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
