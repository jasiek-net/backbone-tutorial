from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from models import User
from django.http import HttpResponse, JsonResponse
import json

@csrf_exempt
def users(request):
    if request.method == "POST":
        print 'Raw Data: "%s"' % request.body
        user = User()
        data = json.loads(request.body)
        user.firstname = data['firstname']
        user.lastname = data['lastname']
        user.age = data['age']
        user.save()
    response = JsonResponse(list(User.objects.values()), safe=False)
    return response

@csrf_exempt
def user(request, id):
    if request.method == "GET":
        user = User.objects.filter(id=id).values()
        return JsonResponse(dict(user[0]), safe=False)
    elif request.method == "PUT":
        user = User.objects.filter(id=id)[0]
        print 'Raw Data: "%s"' % user
        data = json.loads(request.body)
        user.firstname = data['firstname']
        user.lastname = data['lastname']
        user.age = data['age']
        user.save()
        return JsonResponse(serializers.serialize('json', [user,]), safe=False)
    elif request.method == "DELETE":
        user = User.objects.filter(id=id)[0]
        user.delete()
        return JsonResponse({'res':'ok'}, safe=False)

