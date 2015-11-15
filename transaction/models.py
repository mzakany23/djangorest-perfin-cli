from django.db import models

class Transaction(models.Model):
	CATEGORIES = (
		('Fixed','fixed'),
		('Variable','variable'),
		('Income', 'income'),
	)
	category = models.CharField(max_length=40,choices=CATEGORIES,blank=True,null=True)
	account = models.ForeignKey('Account')
	date = models.DateField(blank=True,null=True)
	check_number = models.CharField(max_length=40,blank=True,null=True)
	name = models.CharField(max_length=250,blank=True,null=True)
	amount = models.DecimalField(max_digits=6,decimal_places=2,default=0.00)
	timestamp = models.TimeField(auto_now_add=True,blank=True,null=True)

	class Meta:
		unique_together = (("date", "check_number", "name",'amount'),)

	def __unicode__(self):
		return self.account.title


class Account(models.Model):
	active = models.BooleanField(default=True)
	TYPES = (
		('Checking','checking'),
		('Credit Card','credit card'),
	)
	type = models.CharField(max_length=40,choices=TYPES,blank=True,null=True)
	title = models.CharField(max_length=40)
	slug = models.SlugField(max_length=50,blank=True,null=True)

	def __unicode__(self):
		return self.title


