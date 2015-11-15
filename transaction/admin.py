from django.contrib import admin
from models import Transaction,Account

class TransactionAdmin(admin.ModelAdmin): 
	list_display = ['account','check_number','date','name','amount','timestamp']
	class Meta:
		model = Transaction

admin.site.register(Transaction,TransactionAdmin)

class AccountAdmin(admin.ModelAdmin): 
	prepopulated_fields = {"slug": ("title",)}
	list_display = ['title','active','type']
	list_editable = ['active']
	class Meta:
		model = Account

admin.site.register(Account,AccountAdmin)
