from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

from api.helper.paginator_helper import APIGenericGenerator

from transaction.models import Account,Transaction
from api.transaction.serializers import TransactionSerializer

class RIOTAPITransactions(APIView):
	def get(self,request,slug,format=None):
		try:
			account = Account.objects.get(slug=slug)
			transactions = Transaction.objects.filter(account=account).order_by('-date')
		except:
			transactions = None 
		if transactions:
			trans = APIGenericGenerator(queryset=transactions,serializer=TransactionSerializer)
			return Response(trans.list_paginated_results(request))
		else:
			return Response('Failure')