import pandas as pd
import requests
import sys
from datetime import datetime, timedelta
import math
import csv

class GroupByWordList:
	def __init__(self,url,wordlist):
		self.url = url 
		self.wordlist = wordlist
		self.results = {'unfound' : []}

	def run(self):
		req = requests.get(self.url)
		df = pd.read_json(req.text)

		for row in df.iterrows():

			amount = row[1][1]
			date = row[1][2]
			name = row[1][3]

			if math.isnan(amount):
				amount = 0.00

			formatted_name = name.lower().split(' ')

			summed_amount = 0

			found_transaction = False

			for word in self.wordlist:
				if word in formatted_name:

					found_transaction = True

					formatted_row = {
						'date' : date.date(),
						'name' : name,
						'amount' : amount,
					}

					try:
						# if self.results[word]['data'].count(formatted_row) < 2:
						# 	self.results[word]['data'].append(formatted_row)
						# 	self.results[word]['sum'] += float(amount)
						if not formatted_row in self.results[word]['data']:
							self.results[word]['data'].append(formatted_row)
							self.results[word]['sum'] += float(amount)
					except:
						self.results[word] = {
							'data' : [],
							'sum' : 0,
						}
						self.results[word]['data'].append(formatted_row)
						self.results[word]['sum'] += float(amount)
				
				
			if not found_transaction:
				self.results['unfound'].append({'date' : date,'name' : name,'amount' : amount})
		return self

	def show(self):
		print 'found'
		for key,value in self.results.items():
			if key != 'unfound':
				for row in value['data']:
					print row
				print value['sum']

		print 'unfound'
		for row in self.results['unfound']:
			print row

	def to_csv(self,url):
		if url:
			with open(url, 'wb') as csvfile:
			    w = csv.writer(csvfile)
			    w.writerow(['key', 'date', 'description','amount','total','count','average'])
			    for key,value in self.run().results.items():
			    	if key != 'unfound':
				    	w.writerow([key])
				    	for row in value['data']:
				    		w.writerow(['',row['date'],row['name'],row['amount']])
				    		sum_amt = value['sum']
				    		count = len(value['data'])
				    		average = "%.2f" % round((sum_amt/count),2)

				    	w.writerow(['','','','',sum_amt,count,average])
		else:
			raise Exception('have to put url brah')


# url = 'http://localhost:8001/api/transactions/fifth-third/?from=11/01/2015&to=11/30/2015'
# x = GroupByWordList(url,['electronic'])
# x.run().to_csv('x.csv')



