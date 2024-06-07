from rest_framework import generics
from student.models import Student
from student.serailzers import StudentSerializer, StudentRetrieveSerializer, StudentUpdateSerializer


class StudentCreateView(generics.CreateAPIView):
    serializer_class = StudentSerializer


class StudentRetrieveView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentRetrieveSerializer

    def get_queryset(self):
        student_id = self.kwargs['pk']
        course_id = self.kwargs['course_id']
        #TODO : implement filter class and filter backend
        queryset = self.queryset.filter(pk=student_id, course_id=course_id)
        return queryset


class StudentUpdateView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer

