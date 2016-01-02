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