from django.shortcuts import render_to_response
from django.http import httpResponse, httpResponseRedirect
from django.shortcuts import get_object_or_404

# index page
def index(request):
	return HttpResonseRedirect('/')