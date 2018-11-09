# okay.. lets start from where we are: reading in available data

import random
from datetime import datetime, timedelta

file = open("sales_and_alerts.csv")

head = file.readline().strip().split(",")
data = [line.strip().split(",") for line in file.readlines()]

# no time stamps, generate some
# assume same day

dataset_size = len(data)
time_stamps = []

for _ in range(dataset_size):
	# assume working hours: 7am to 7pm
	hour = random.choice(range(7,20))
	min = random.choice(range(60))
	time_stamp = "{:0>2s}:{:0>2s}".format(str(hour), str(min))
	time_stamps.append(time_stamp)


time_stamps.sort()

# relevant columns are time stamp and price
prices = [row[4] for row in data]
dataset = [row for row in zip(prices, time_stamps)]

# identified edge cases:
	# early payment: 0
	# late payment: 1
	# split payment (assume 2 installments): 2
	
	# normal (1 min before sale): 3

# intent is to randomise alerts
cases = [0, 1, 2, 3]

def early_pmt(tm_stamp, price):
	# 5 to 30 mins early
	diff_in_mins = random.choice(range(5, 30))
	diff_in_secs = diff_in_mins * 60
	
	hr, min = tm_stamp.split(":")
	sales_time = datetime(2018, 11, 12, int(hr), int(min))
	
	alert_time = sales_time - timedelta(seconds=diff_in_secs)
	return alert_time, price

def late_pmt(tm_stamp, price):
	# 5 to 30 mins late
	diff_in_mins = random.choice(range(5, 30))
	diff_in_secs = diff_in_mins * 60
	
	hr, min = tm_stamp.split(":")
	sales_time = datetime(2018, 11, 12, int(hr), int(min))
	
	alert_time = sales_time + timedelta(seconds=diff_in_secs)
	return alert_time, price

def normal_pmt(tm_stamp, price):
	# a minute early
	diff_in_secs = 60
	
	hr, min = tm_stamp.split(":")
	sales_time = datetime(2018, 11, 12, int(hr), int(min))
	
	alert_time = sales_time - timedelta(seconds=diff_in_secs)
	return alert_time, price

def split_pmt(tm_stamp, price):
	# a payment before and another after
	tm_before = early_pmt(tm_stamp, price)[0]
	tm_after = late_pmt(tm_stamp, price)[0]
	
	pr_before = int(price) * 0.75
	pr_after = int(price) * 0.25
	
	return [tm_before, pr_before], [tm_after, tm_after]