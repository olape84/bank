import requests,csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=csv")
data = response.json()
print(response)
print(data)
from pprint import pprint
pprint(data)
rates=data[0]["rates"]
with open("data.csv", "w") as file:
   writer = csv.writer(file)
   writer.writerow(['currency', 'code' 'bid'])
   for row in rates:
      writer.writerow([row['currency'], row ['code'], row['bid']])