from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import Request,Response

def home(request):
    return HttpResponse("Hello world")


@api_view(['GET','POST'])
def events(request:Request):
    if request.method == 'GET':
        return Response(data = {"message":"This is the GET events endpoint"},status = 200)
        
    elif request.method == 'POST':
        return Response(data = {"message":"This is the POST events endpoint"},status = 200)

@api_view(['GET','POST'])
def reservations(request:Request):
    if request.method == 'GET':
        return Response(data = {"message":"This is the reservations GET endpoint"},status = 200)
    
    elif request.method == 'POST':
        return Response(data = {"message":"This is the reservations POST endpoint"},status = 200)
