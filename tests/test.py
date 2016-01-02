from datetime import datetime
import calendar
import requests

import sys
sys.path.append('../')

from scripts.analysis import GroupByWordList

def to_date_range(month=None,year=None):
	if month is not None and year is not None:
		dates = {
			'jan' : 1,
			'feb' : 2,
			'mar' : 3,
			'apr' : 4,
			'may' : 5,
			'jun' : 6,
			'jul' : 7,
			'aug' : 8,
			'sep' : 9,
			'oct' : 10,
			'nov' : 11,
			'dec' : 12
		}

		m = dates[month]
		d = calendar.monthrange(year,m)[1]

		return (("%s/1/%s" % (m,year)),("%s/%s/%s" % (m,d,year)))
	else:
		t = datetime.today()
		m = t.month
		y = t.year
		d = calendar.monthrange(y,m)[1]
		return (("%s/1/%s" % (m,y)),("%s/%s/%s" % (m,d,y)))

FIXED_LIST = ['paypal','paid','alert','electronic','jeanie','payment','nissan','navient','natl','lmcu']
VARIABLE_LIST = ['paypal','chipotle','wrnr','fitness','phoenix','wholefds','starbucks','cvs/pharmacy','utilitie','cinemas','cinemark','yoga','oil','la','theatre','fc34','payment']

# print to_date_range()

# print to_date_range('dec',2015)

# url = "http://localhost:8001/api/transactions/chase-united/?from=%s&to=%s" % (dr[0],dr[1])

x = GroupByWordList(url,FIXED_LIST)


# print x.run().show()


# x.run().to_csv('/Users/mzakany/Desktop/x.csv')


# perfin report fifth-third 12/01/2015 12/30/2015 -w paypal,paid,alert,electronic,jeanie,payment,nissan,navient,natl,lmcu -f fifth-third.csv

# perfin report chase-united 12/01/2015 12/30/2015 -w paypal,chipotle,wrnr,fitness,phoenix,wholefds,starbucks,'cvs/pharmacy',utilitie,cinemas,cinemark,yoga,oil,la,theatre,fc34,payment -f chase-united.csv






# print to_date_range('feb',2015)

# today = datetime.today()
# print datetime.today().month

# print datetime.strftime(today,"%m/%d/%Y")