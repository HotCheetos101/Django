from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Added
from rest_framework.views import APIView
from rest_framework.response import Response

def homepage(request):
    return render(request,'index.html')


class HelloView(APIView):
    def get(self, request):
        return Response({'message': 'Hello, world!'})
    
    


