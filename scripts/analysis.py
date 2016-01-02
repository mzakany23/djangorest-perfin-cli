import pandas as pd
import requests
import sys
from datetime import datetime, timedelta
import math
import csv

class GroupByWordList:
	def __init__(self,url,wordlist):
		self.url = url 
		# wordlist is a string like 'foo,bar'
		self.wordlist = wordlist
		self.results = {'unfound' : {}}
		self.totals = {
			'unfound' : {'sum' : 0},
			'found' : {'sum' : 0}
 		}

 	def get_totals(self):
 		return self.totals

	def run(self):
		req = requests.get(self.url)
		df = pd.read_json(req.text)

		for row in df.iterrows():

			amount = row[1][1]
			date = row[1][2]
			name = row[1][3]

			if math.isnan(amount):
				amount = 0.00

			formatted_name = name.lower().replace('*','').split(' ')

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
						if not formatted_row in self.results[word]['data']:
							self.results[word]['data'].append(formatted_row)
							self.results[word]['sum'] += float(amount)
							self.totals['found']['sum'] += float(amount)
					except:
						self.results[word] = {
							'data' : [],
							'sum' : 0,
						}
						self.results[word]['data'].append(formatted_row)
						self.results[word]['sum'] += float(amount)
						self.totals['found']['sum'] += float(amount)
				
		
			if not found_transaction:
				
				formatted_transaction = {'date' : date.strftime("%m/%d/%Y"),'name' : name,'amount' : amount}
				key = name[:8]
				

				try:
					if key in self.results['unfound']:
						if formatted_transaction not in self.results['unfound'][key]['data']:
							self.results['unfound'][key]['data'].append(formatted_transaction)
							self.results['unfound'][key]['sum'] += float(amount)
							self.totals['unfound']['sum'] += float(amount)
					else:
						self.results['unfound'][key] = {
						'data' : [],
						'sum' : 0
						}
						self.results['unfound'][key]['data'].append(formatted_transaction)
						self.results['unfound'][key]['sum'] += float(amount)	
						self.totals['unfound']['sum'] += float(amount)
						
				except KeyError:
					pass
		
		return self	


	def show(self):
		print 'found'
		for key,value in self.results.items():
			if key != 'unfound':
				print key
				for row in value['data']:
					print row
				print value['sum']

		print 'unfound'
		for key,value in self.results['unfound'].items():
			print key
			print value

	def to_csv(self,url):
		if url:
			with open(url, 'wb') as csvfile:
			    w = csv.writer(csvfile)
			    run_obj = self.run()
			    results = run_obj.results
			    totals = run_obj.get_totals()
			    w.writerow([''])
			    w.writerow(['transaction','total'])
			    w.writerow(['found',totals['found']['sum']])
			    w.writerow(['unfound',totals['unfound']['sum']])
			    w.writerow([''])

			    w.writerow(['key', 'date', 'description','amount','total','count','average'])
			    
			    for key,value in results.items():
			    	if key != 'unfound':
			    		w.writerow([key])
				    	for row in value['data']:
				    		w.writerow(['',row['date'],row['name'],row['amount']])
				    		sum_amt = value['sum']
				    		count = len(value['data'])
				    		average = "%.2f" % round((sum_amt/count),2)

				    	w.writerow(['','','','',sum_amt,count,average])
			    	else:
			    		w.writerow([''])
			    		w.writerow(['unfound transactions:'])
			    		w.writerow([''])

			    		for key,value in results['unfound'].items():
			    			w.writerow([key])
			    			for item in value['data']:
			    				w.writerow(['',item['date'],item['name'],item['amount']])
			    				sum_amt = value['sum']
			    				count = len(value['data'])
			    				average = "%.2f" % round((sum_amt/count),2)
			    			w.writerow(['','','','',sum_amt,count,average])

			    		w.writerow([''])
			    		w.writerow(['found transactions'])
			    		w.writerow([''])

		else:
			raise Exception('have to put url brah')

