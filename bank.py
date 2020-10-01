import csv

with open ('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

file=open("data.csv", "w")
writer = csv.writer(file)
writer.writerow(["currency","bid"])

@app.route('/')
def home:
  return currency

@app. route('/calculation')
  def calculation:
    result = amount * bid
  return result