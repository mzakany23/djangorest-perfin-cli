import pandas as pd
import requests
import sys
from datetime import datetime, timedelta
sys.path.append('/Users/mzakany/Desktop/perfin_2015/helper')

from perfin import Perfin

# ----------------------------------------------------------------------------------
# files
# ----------------------------------------------------------------------------------

# path = "/Users/mzakany/Desktop/53.CSV"
# path = "/Users/mzakany/Desktop/chase-united.CSV"
# path = "/Users/mzakany/Desktop/capitalone-venture.CSV"
# path = "/Users/mzakany/Desktop/capitalone-signature.CSV"

# csv = Perfin(path)

# data = csv.to_json()

# url = 'http://localhost:8001/api/transactions/chase-united/?from=10/01/2015&to=10/31/2015'
# url = 'http://localhost:8001/api/transactions/'

# get_transactions = requests.get(url)

# ----------------------------------------------------------------------------------
# posts
# ----------------------------------------------------------------------------------

# p = requests.post("http://localhost:8001/api/upload-transactions/fifth-third/", data={"data": data,'type' : 'Fifth Third'})
# p = requests.post("http://localhost:8001/api/upload-transactions/chase-united/", data={"data": data,'type' : 'Chase United'})
# p = requests.post("http://localhost:8001/api/upload-transactions/capital-one-venture/", data={"data": data,'type' : 'Capital One Venture'})
# p = requests.post("http://localhost:8001/api/upload-transactions/capital-one-signature/", data={"data": data,'type' : 'Capital One Signature'})

# print p

# ideally be this:
# perfin upload /Users/mzakany/Desktop/folder

# pd.read_json(get_transactions.text)[['account','date','name','amount']].to_csv('/Users/mzakany/Desktop/x.csv')

# for row in pd.read_json(get_transactions.text)[['account','date','name','amount']].iterrows():
# 	print row[1][0]['slug']
# 	print row[1][1]
# 	print row[1][2]
# 	print row[1][3]

# req = requests.post("http://localhost:8001/api/search-by-wordlist/?account=fifth-third&from=10/01/2015&to=10/31/2015", data={"wordlist": 'musical,paypal'})

# print req


