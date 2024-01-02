from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

class ToDoAPIView(APIView):
    def get(self, request):
        return Response({"message": "This is the ToDo API."})

    
def toDo_page(request):
    return render(request, "toDo/toDo.html")
