from django.shortcuts import render
from rest_framework.filters import SearchFilter,OrderingFilter
from . models import Student
from rest_framework.generics import(ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView)
from . serializers import StudentSerializer
from .pagination import Pag
# Create your views here.

class StudentListApiView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer  
    filter_backends=[SearchFilter]
    search_fields = ['id', 'name','roll']
    # pagination_class=Pag  



class StudentDetailApiView(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer  
    lookup_field='name'  
    

class StudentUpdateApiView(UpdateAPIView,RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer  
    lookup_field='name'  
    

class StudentDestroyApiView(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer  
    lookup_field='name'  
    

class StudentCreateApiView(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer 

    def  perform_create(self,serializer):
        serializer.save(user=self.request.user)
