# python
import sys
import os
import shutil
from os.path import basename, abspath
from optparse import OptionParser
import requests
import pandas as pd
# app
from analysis import GroupByWordList
from config import WordList
from lib.helper import to_date_range,today


parser = OptionParser(version="0.0.1")
parser.add_option("-f", "--file", dest="filename",help="save csv to (usually on desktop)", metavar="FILE")
parser.add_option("-w", "--wordlist",dest="wordlist",help="search by wordlist")
parser.add_option("-$", "--amount",dest="amount",help="search by amounts")
parser.add_option("-t", "--type",dest="type",help="report type")
parser.add_option("-d", "--date",dest="date",help="date")

options, args = parser.parse_args()


if not args:
	sys.stdout.write('use like this:     perfin get fifth-third 10/01/2015 10/31/2015 -f file.csv     ')
	exit(2)
else:
	
	if len(args) == 4:
		action = args[0]
		account = args[1]
		from_date = args[2]
		to_date = args[3]

		if action == 'report':
			
			if account == 'all':
				url = "http://localhost:8001/api/transactions/?from=%s&to=%s" % (from_date,to_date)

				if options.wordlist:
					wordlist = options.wordlist.split(',')
					x = GroupByWordList(url,wordlist)
					if options.filename and action == 'report':
						x.run().to_csv(str(options.filename))
					else:
						print 'ok here i am'
						x.run().show()
				
			else:

				url = "http://localhost:8001/api/transactions/%s/?from=%s&to=%s" % (account,from_date,to_date)
				if options.wordlist:
					wordlist = options.wordlist.split(',')
					x = GroupByWordList(url,wordlist)
					if options.filename and action == 'report':
						x.run().to_csv(str(options.filename))
					else:
						x.run().show()

		# search by amounts
		if options.amount and len(options.amount.split(',')) == 2:
			amounts = options.amount.split(',')
			min = amounts[0]
			max = amounts[1]
			url = 'http://localhost:8001/api/search-by-amounts/?account=%s&min=%s&max=%s&from=%s&to=%s' % (account,min,max,from_date,to_date)
			req = requests.get(url)
			if options.filename:
				if req.status_code == 200 and options.filename:
					pd.read_json(req.text).to_csv(options.filename)
				else:
					print req
			exit(2)

		if account == 'all' and not options.wordlist:
			url = 'http://localhost:8001/api/transactions/?from=%s&to=%s' % (from_date,to_date)
		else:
			url = "http://localhost:8001/api/search-by-wordlist/?account=%s&from=%s&to=%s" % (account,from_date,to_date)

		if account != 'all' and options.wordlist:
			wordlist = options.wordlist
			url = "http://localhost:8001/api/search-by-wordlist/?account=%s&from=%s&to=%s" % (account,from_date,to_date)
			get_transactions = requests.post(url, data={"wordlist": wordlist})
		elif account == 'all' and options.wordlist:
			wordlist = options.wordlist
			url = "http://localhost:8001/api/search-by-wordlist/?account=%s&from=%s&to=%s" % (account,from_date,to_date)
			get_transactions = requests.post(url, data={"wordlist": wordlist})
		elif account != 'all' and not options.wordlist:
			url = 'http://localhost:8001/api/transactions/%s/?from=%s&to=%s' % (account,from_date,to_date)
			get_transactions = requests.get(url)
			df = pd.read_json(get_transactions.text)[['date','name','amount']]
			# df.sort('date',ascending=False)
			df.drop_duplicates().to_csv(options.filename)

			exit(2)
		else:
			get_transactions = requests.get(url)

		if options.filename and action != 'report':
			filename = options.filename
			pd.read_json(get_transactions.text)[['account','date','name','amount']].to_csv(filename)
		else:
			# print pd.read_json(get_transactions.text)[['account','date','name','amount']]
			pass

	
	if len(args) == 2:

		if args[1] == 'all' and not options.wordlist:
			url = 'http://localhost:8001/api/transactions/'
			get_transactions = requests.get(url)
			if options.filename:
				filename = options.filename
				pd.read_json(get_transactions.text)[['account','date','name','amount']].to_csv(filename)
			else:
				print pd.read_json(get_transactions.text)[['account','date','name','amount']]
		else:
			# do a net income calculation
			# needs finished
			if options.type:
				account = args[1]
				date = options.date.split('-')
				fd,td = date[0],date[1]
				min,max = 0,20000
				if options.type and options.date:
					url = 'http://localhost:8001/api/search-by-amounts/?account=%s&min=%s&max=%s&from=%s&to=%s' % (account,min,max,from_date,to_date)
					req = requests.get(url)
				else:
					exit(2)


				

			if options.wordlist:
				wordlist = options.wordlist
				
				if args[1] != 'all' and wordlist:
					req = requests.post(
						"http://localhost:8001/api/search-by-wordlist/?account=%s" % args[1], 
						data={
							"wordlist": wordlist,
					})
				else:
					req = requests.post(
						"http://localhost:8001/api/search-by-wordlist/", 
						data={
							"wordlist": wordlist,
					})

				if options.filename:
					res = pd.read_json(req.text)
					res.to_csv(options.filename)

			else:
				action = args[0]
				account = args[1]

				url = 'http://localhost:8001/api/transactions/%s' % account
				get_transactions = requests.get(url)


				if options.filename:
					filename = options.filename
					pd.read_json(get_transactions.text)[['account','date','name','amount']].to_csv(filename)
				else:
					print pd.read_json(get_transactions.text)[['account','date','name','amount']]

	if len(args) == 1:
		if args[0] == 'myreport':
			dr = to_date_range()
			
			ft_url = "http://localhost:8001/api/transactions/fifth-third/?from=%s&to=%s" % (dr[0],dr[1])
			cu_url = "http://localhost:8001/api/transactions/chase-united/?from=%s&to=%s" % (dr[0],dr[1])
			
			payload = GroupByWordList(ft_url,WordList.FIXED_LIST)
			payload = GroupByWordList(cu_url,WordList.VARIABLE_LIST)
			
			dd = WordList.DEFAULT_DIR

			ft_loc = "%s/fifth-third-%s.csv" % (dd,today())
			cu_loc = "%s/chase-united-%s.csv" % (dd,today())
			
			payload.run().to_csv(ft_loc)
			payload.run().to_csv(cu_loc)

		if args[0] == 'upload':
			
			file = options.filename
			
			if file and file == 'all':
				# upload specific file
				pass
			else:
				

				for file in os.listdir('/Users/mzakany/Desktop/perfin_2015/files'):

					if file.endswith('.csv') or file.endswith('.CSV'):
						full_file_name = os.getcwd()+'/perfin_2015/files/%s' % file

						
						f = os.path.splitext(full_file_name)[0]
						filename = basename(f)
						
						csv = pd.read_csv(full_file_name)
						data = csv.to_json()

						if filename in ['53','fifth-third','fifth-third-bank']:
							requests.post(
								"http://localhost:8001/api/upload-transactions/fifth-third/", 
								data={"data": data,
								'type' : 'Fifth Third'
							})
						elif filename in ['chase','chase-united','united']:
							requests.post(
								"http://localhost:8001/api/upload-transactions/fifth-third/", 
								data={"data": data,
								'type' : 'Chase United'
							})
						elif filename in ['capitalone-venture','capital-one-venture']:
							requests.post(
								"http://localhost:8001/api/upload-transactions/fifth-third/", 
								data={"data": data,
								'type' : 'Capital One Venture'
							})
						elif filename in ['capitalone-signature','capital-one-signature','capital-one-sig']:
							requests.post(
								"http://localhost:8001/api/upload-transactions/fifth-third/", 
								data={"data": data,
								'type' : 'Capital One Signature'
							})

	