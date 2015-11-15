# django
from django.http import Http404
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework import serializers, routers, viewsets,permissions
from rest_framework import pagination

# app
from transaction.models import Transaction,Account

class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account 
		fields = [
			'title'	
			# 'active',
			# 'type',
			# 'slug',
			
		]

class TransactionSerializer(serializers.Serializer):
	account = AccountSerializer(read_only=True)
	date = serializers.DateField()
	name = serializers.CharField(max_length=40)
	amount = serializers.DecimalField(max_digits=6,decimal_places=2)



