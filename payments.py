# functions to generate payment alerts

import random
from datetime import datetime, timedelta


def normal_pmt(tm_stamp, price):
	# a minute early
	diff_in_secs = 60
	
	hr, min = tm_stamp.split(":")
	sales_time = datetime(2018, 11, 12, int(hr), int(min))
	
	alert_time = sales_time - timedelta(seconds=diff_in_secs)
	return [(alert_time, price)]

def early_pmt(tm_stamp, price):
	# 5 to 30 mins early
	diff_in_mins = random.choice(range(5, 30))
	diff_in_secs = diff_in_mins * 60
	
	hr, min = tm_stamp.split(":")
	sales_time = datetime(2018, 11, 12, int(hr), int(min))
	
	alert_time = sales_time - timedelta(seconds=diff_in_secs)
	return [(alert_time, price)]

def late_pmt(tm_stamp, price):
	# 5 to 30 mins late
	diff_in_mins = random.choice(range(5, 30))
	diff_in_secs = diff_in_mins * 60
	
	hr, min = tm_stamp.split(":")
	sales_time = datetime(2018, 11, 12, int(hr), int(min))
	
	alert_time = sales_time + timedelta(seconds=diff_in_secs)
	return [(alert_time, price)]

def split_pmt(tm_stamp, price):
	# a payment before and another after
	tm_before = early_pmt(tm_stamp, price)[0][0]
	tm_after = late_pmt(tm_stamp, price)[0][0]
	
	pr_before = int(price) * 0.75
	pr_after = int(price) * 0.25
	
	return [(tm_before, pr_before), (tm_after, pr_after)]
