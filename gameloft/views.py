from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import json
# from .models import Article, Category
# Create your views here.
def index(request):
	return HttpResponse(loader.get_template('gameloft/index.html').render())

def eva(request):
	return HttpResponse(json.JSONEncoder().encode({"data": {"url":"http://localhost:8000/pandora"}}), content_type="application/json")
	# return HttpResponse(loader.get_template('gameloft/eva.html').render())

@csrf_exempt
def pandora(request):
	if(request.method == 'GET'):
		return HttpResponse(json.JSONEncoder().encode({"status": 500, "message": "Method not allowed"}), content_type="application/json")
	else:
		return HttpResponse(json.JSONEncoder().encode({"status": 200, "data": [{"url1": "http://localhost:8000/otherURL"}, {"url2": "http://localhost:8000/otherURL2"}]}), content_type="application/json")