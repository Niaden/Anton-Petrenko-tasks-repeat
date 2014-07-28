from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.http.request import HttpRequest
from .models import Request
from .forms import RequestForm

# Create your views here.
def showrequests(request):
 	return render(request,'showrequests.html', {'requests': Request.objects.all()})	

def somefunc(request):
	# pl = Request.objects.get(request_date='2014-07-28 11:22:01')
	# pl.request_path = 'omgomgogo/sdsd'
	# pl.save() 
	# Request(request_date='2014-07-28 11:22:01',
	# 	request_path='/showlist/suka/'
	# 	request_method='GET')
	# p.save()
	return HttpResponse('lololo')
