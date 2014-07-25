from django.db import models

# Create your models here.

class Item(models.Model):
	class Meta():
		db_table="lalala_name_buying_list"
	item_name = models.CharField(max_length = 200)
	item_num = models.IntegerField(default = 1)
	item_measure = models.CharField(max_length = 200)