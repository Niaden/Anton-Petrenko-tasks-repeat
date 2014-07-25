# coding: utf8
from django.db import models

# Create your models here.

class Item(models.Model):
	class Meta():
		db_table="buying_list"
	item_name = models.CharField(max_length = 200)
	item_num = models.IntegerField(default = 1)
	item_measure = models.CharField(max_length = 200)
	# item_date - показывает дату, когда нужно купить данный итем
	item_date = models.DateField()

	def __unicode__(self):
		return "{} - {} {} {}".format(self.item_name, self.item_num, self.item_measure, self.item_date)
