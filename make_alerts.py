
import random
import payments as pmt

file = open("sales_and_alerts.csv")

head = file.readline().strip().split(",")
data = [line.strip().split(",") for line in file.readlines()]

# no time stamps, generate some
# assume same day

time_stamps = []
for _ in range(len(data)):
    # randomise time of sales
	# assume working hours: 7am to 7pm
	hour = random.choice(range(7,20))
	min = random.choice(range(60))
	time_stamp = "{:0>2s}:{:0>2s}".format(str(hour), str(min))
	time_stamps.append(time_stamp)

# sort generated time stamps in chronological order
time_stamps.sort()

# relevant columns are time stamp and price
prices = [row[4] for row in data]
dataset = [row for row in zip(prices, time_stamps)]

# sales dataset
with open('sales.csv', 'w') as sales_file:
    sales_file.write('product_id,price,time_stamp\n')

    for row in enumerate(dataset):
        sales_file.write(f'{row[0]},{row[1][0]},{row[1][1]}\n')


# alerts dataset
pmts = [pmt.normal_pmt, pmt.early_pmt, pmt.late_pmt, pmt.split_pmt]

with open('alerts.csv', 'w') as alerts_file:
    alerts_file.write('product_id,payment,time_stamp\n')

    for row in enumerate(dataset):
        pmt = random.choice(pmts)
        product_id = row[0]
        price, tm_stamp = row[1]

        generated_alerts = pmt(tm_stamp, price)
        for alert in generated_alerts:
            tm, pr = alert
            alerts_file.write(f'{product_id},{pr},{tm.hour}:{tm.minute}\n')