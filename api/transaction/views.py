# python 
import pandas as pd
from datetime import datetime

# django
from django.utils.text import slugify
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Q

# app
from transaction.models import Transaction,Account
from serializers import TransactionSerializer
from form import TransactionForm

class FilterByWordListViewSet(APIView):
	def post(self,request):
		try:
			account_slug = request.GET['account']
			if not account_slug == 'all':
				account = Account.objects.get(slug=account_slug)
		except:
			account_slug = None
			account = None

		try:
			from_date = datetime.strptime(request.GET['from'],"%m/%d/%Y").strftime("%Y-%m-%d")
			to_date = datetime.strptime(request.GET['to'],"%m/%d/%Y").strftime("%Y-%m-%d")
		except:
			from_date = None 
			to_date = None 

		try:
			post_word_list = request.POST.getlist('wordlist')
			wordlist =  str(post_word_list[0]).split(',')
			
			if account_slug == 'all' and from_date and to_date:
				transactions = Transaction.objects.filter(reduce(lambda x, y: x | y, [Q(name__contains=word) for word in wordlist])).filter(date__range=[from_date,to_date]).order_by('-date')
			elif account and from_date and to_date:
				transactions = Transaction.objects.filter(account=account).filter(reduce(lambda x, y: x | y, [Q(name__contains=word) for word in wordlist])).filter(date__range=[from_date,to_date]).order_by('-date')
			elif account:
				transactions = Transaction.objects.filter(account=account).filter(reduce(lambda x, y: x | y, [Q(name__contains=word) for word in wordlist]))
			else:
				transactions = Transaction.objects.filter(reduce(lambda x, y: x | y, [Q(name__contains=word) for word in wordlist])).order_by('-date')

			
			serializer_class = TransactionSerializer
			serializer = TransactionSerializer(transactions,many=True)

			return Response(serializer.data,status=status.HTTP_200_OK)
		except:
			return Response('no good brah',status=status.HTTP_204_NO_CONTENT)

class AllTransactionsViewSet(APIView):

	def get(self,request):
		try: 
			if request.GET:
				try:
					from_date = datetime.strptime(request.GET['from'],"%m/%d/%Y").strftime("%Y-%m-%d")
					to_date = datetime.strptime(request.GET['to'],"%m/%d/%Y").strftime("%Y-%m-%d")
					transactions = Transaction.objects.filter(date__range=[from_date,to_date]).order_by('-date')
				except:
					transactions = Transaction.objects.all()
			else:
				transactions = Transaction.objects.all()
		except:
			return Response('blown up dude')

		serializer_class = TransactionSerializer
		serializer = TransactionSerializer(transactions,many=True)

		return Response(serializer.data,status=status.HTTP_200_OK)


class TransactionsViewSet(APIView):

	def get(self,request,slug):
		# for x in Transaction.objects.all():
		# 	if Transaction.objects.filter(name=x.name,date=x.date,amount=x.amount).count() == 6:
		# 		print x.name
		try:
			account = Account.objects.get(slug=slug)
			if request.GET:
				try:
					from_date = datetime.strptime(request.GET['from'],"%m/%d/%Y").strftime("%Y-%m-%d")
					to_date = datetime.strptime(request.GET['to'],"%m/%d/%Y").strftime("%Y-%m-%d")
					transactions = Transaction.objects.filter(account=account).filter(date__range=[from_date,to_date]).order_by('-date')
				except:
					transactions = Transaction.objects.filter(account=account).filter(account__active=True).order_by('-date')
			else:
				transactions = Transaction.objects.filter(account=account).filter(account__active=True).order_by('-date')

		except:
			transactions = None

		if not transactions:
			return Response('no transactions dude',status=status.HTTP_204_NO_CONTENT)

		serializer_class = TransactionSerializer
		serializer = TransactionSerializer(transactions,many=True)
		return Response(serializer.data,status=status.HTTP_200_OK)

class UploadTransactionsViewSet(APIView):

	def get_table_headers_by_account(self,account):
		if account == 'fifth-third':
			return ['Date','Description','Amount','Check Number']
		elif account == 'chase-united':
			return ['Post Date','Description','Amount']
		elif account == 'capital-one-venture' or account == 'capital-one-signature':
			return [5,4,3]

	def get_index_location_by_account(self,account):
		if account == 'fifth-third':
			data = {
				'date' : [1,0],
				'name' : [1,1],
				'amount' : [1,2],
				'check_number' : [1,3]
			}
		if account == 'chase-united':
			data = {
				'date' : [1,0],
				'name' : [1,1],
				'amount' : [1,2],
			}

		if account == 'capital-one-venture' or account == 'capital-one-signature':
			data = {
				'date' : [1,0],
				'name' : [1,1],
				'amount' : [1,2],
			}


		return data

	def post(self,request,slug):
		try:
			data = request.POST['data']
			type = request.POST['type']
			account = Account.objects.get(slug=slugify(type))
		except:
			return Response('wrong post parameters dude',status=status.HTTP_204_NO_CONTENT)

		transaction_set = pd.read_json(data)[self.get_table_headers_by_account(account.slug)]

		data = self.get_index_location_by_account(account.slug)

		for row in transaction_set.iterrows():	
			name = str(row[data['name'][0]][data['name'][1]])
			amount = float(row[data['amount'][0]][data['amount'][1]])

			try:
				data['check_number']
				date = row[data['date'][0]][data['date'][1]].to_pydatetime().date()
				check_number = str(row[data['check_number'][0]][data['check_number'][1]])
				transaction_exists = Transaction.objects.filter(
					date=date,
					name=name,
					amount=amount,
					check_number=check_number
				).exists()
			except:
				date = datetime.strptime(row[data['date'][0]][data['date'][1]],"%m/%d/%Y").date()

				transaction_exists = Transaction.objects.filter(
					date=date,
					name=name,
					amount=amount
				).exists()

			try:
				if not transaction_exists:
					if account == 'fifth-third':
						Transaction.objects.create(
							account=account,
							date=date,
							name=name,
							amount=amount,
							check_number=check_number
						)
					else:
						Transaction.objects.create(
							account=account,
							date=date,
							name=name,
							amount=amount,
						)
			except:
				pass



		return Response('uploaded the transactions',status=status.HTTP_200_OK)
