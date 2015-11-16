import pandas as pd 
import datetime


class Perfin:
	def __init__(self,csv,columns=None,date_range=None):
		self.csv = csv 
		self.columns = columns 
		self.date_range = date_range
		self.results = {}
		
	def to_json(self):
		return pd.read_csv(self.csv).to_json()

	def df(self):
		return pd.read_csv(self.csv)

	def generate_dict(self):
		for row in self._read_csv():
			date = row[1][0]
			name = row[1][1]
			amount = row[1][2]
			# filter date range
			key = name.replace(' ','').lower()[:10]
			transaction = {'date' : date,'name' : name,'amount' : amount}

			try:
				self.results[key].append(transaction)
			except:
				self.results[key] = []
				self.results[key].append(transaction)

		return self


	def to_summary(self):
		for key,value in self.results.items():
			total = 0
			print key
			for item in value:
				total+=item['amount']
				print item
			print total


	# private 

	def _read_csv(self):
		if self.columns and (type(self.columns) == list) and len(self.columns) == 3 and self.csv:
			df = pd.read_csv(self.csv)
			return df[[self.columns[0],self.columns[1],self.columns[2]]].iterrows()
		else:
			return False


# date = '10/08/2015'
# d = datetime.datetime.strptime(date,'%m/%d/%Y').date()
# print d

# chase = 'chase-united.csv'
# chase = '53.csv'
# chase = 'capitalone-venture.csv'
# chase = 'capitalone-sig.csv'

# csv = Perfin(chase).to_json()

# for row in pd.read_json(csv)[['Post Date','Description','Amount']].iterrows():
# 	print row[1][0].__class__
# 	break

# for row in pd.read_json(csv)[['Date','Description','Amount']].iterrows():
# 	print row[1][0].to_pydatetime().date()
# 	break


# print pd.read_json(csv)[[5,4,3]]


