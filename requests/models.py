from django.db import models
from django.http.response import HttpResponse
from django.http.request import HttpRequest
import datetime

# Create your models here.
class Request(models.Model):
	class Meta():
		db_table = "Requests"
	request_date = models.DateTimeField()
	request_method = models.CharField(max_length = 50)
	request_path = models.CharField(max_length = 300)

	def __unicode__(self):
		return "{} {} {}".format(self.request_date,self.request_path,self.request_method)

class WebRequestMiddleware(object):
	def process_request(self, request):
		req_path =  request.get_full_path()
		req_method = request.method
		req_date = datetime.datetime.now()
		request_ob = Request(request_date=req_date, request_method=req_method, request_path=req_path)
		request_ob.save()
		return None
