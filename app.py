import csv
from flask import Flask, request, render_template

app=Flask(__name__) 
 
def get_rate(file_name, currency):
    with open (file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row: 
                if currency==row [0]:
                   return float(row[2])
print(get_rate('data.csv', 'dolar amerykański'))

@app.route('/', methods=['GET', 'POST']) 
def currency():
   if request.method == 'GET':
       return render_template ("form.html")
   elif request.method == 'POST':
       waluta=request.form['waluta']
       ilosc =request.form['ilosc']
       result=get_rate('data.csv', waluta)
       wynik=float(ilosc)*result
       return render_template('form.html', wynik=wynik)#nie rozumiem czemu muszę napisać wynik=wynik

if __name__ == "__main__":
    app.run(debug=True)