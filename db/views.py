from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from db.models import Person


def my_function(request):
    return HttpResponse("Hello, world. You're at the polls page.")

def home_page(request):
    persons = Person.objects.all().values('first_name', 'last_name', 'email')
    print(persons)
    data=list(persons)
    # return HttpResponse("My Home Page using Djang")
    return JsonResponse(data, safe=False)