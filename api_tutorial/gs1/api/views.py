from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializer import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializers(stu)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')


# def student_detail(request):
#     try:
#         stu=Student.objects.get(id=1)
#     except Student.DoesNotExist:
#         return HttpResponse(JSONRenderer().render({"message":"Query not found"}),content_type='application/json')
#     serializer=StudentSerializers(stu)
#     json_data=JSONRenderer().render({"result":serializer.data})
#     return HttpResponse(json_data,content_type='application/json')
