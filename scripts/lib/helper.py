import sys
sys.path.append('../')

from config import WordList
from analysis import GroupByWordList

from datetime import datetime
import calendar


def today():
	return datetime.strftime(datetime.today(),'%d-%m-%Y')

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


def myreport(month=None,year=None):
	if month and year:
		dr = to_date_range(month,year)
	else:
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