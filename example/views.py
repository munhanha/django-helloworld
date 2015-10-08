from django.shortcuts import render

#
from django.http import HttpResponse

#
from django.shortcuts import render_to_response

#
from django.http import JsonResponse

#Simple HttpResponse Example
def helloWorld(request):
	return HttpResponse("Hello, world.")
	
	
#Simple Example using Django Templates and Bootstrap	
def helloWorldTemplate(request):
	return render_to_response('main.html')#, {"foo": "bar"},
						#content_type="application/xhtml+xml")
	
	
#Simple Example	that returns JSON
def helloWorldJSON(request):
	return JsonResponse({'foo':'bar'})