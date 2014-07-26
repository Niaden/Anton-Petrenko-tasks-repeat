from django.db import models

# Create your models here.
class Request(models.Model):
	class Meta():
		db_table = "Requests"
	request_date = models.DateTimeField()
	request_method = models.CharField(max_length = 50)
	request_path = models.CharField(max_length = 300)

	def __unicode__(self):
		return "{} {} {}".format('request_date','request_path','request_method')