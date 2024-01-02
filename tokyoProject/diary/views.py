from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

class DiaryDateSelectionAPIView(APIView):
    def get(self, request):
        return render(request, "diary/date_selection.html")

class DiaryDetailAPIView(APIView):
    def get(self, request, year, month, day):
        date_str = f"{year}-{month}-{day}"
        return render(request, "diary/diary_detail.html", {"date": date_str})
