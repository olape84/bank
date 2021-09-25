import csv
from flask import Flask, request, render_template

app=Flask(__name__) 
 
def get_rate(file_name, currency):
    with open (file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row: 
                if currency==row [1]:
                   return float(row[2])
print(get_rate('data.csv', 'USD'))

@app.route('/', methods=['GET', 'POST']) 
def currency():#nie wiem czy prawidłowo rozumiem tą funkcję:
   if request.method == 'GET': #jeśli zapytanie request to get
       return render_template ("form.html")#to zwraca formularz na stronie
   elif request.method == 'POST':#jeśli zapytanie request to post to ##post nie działa
       waluta=request.form('waluta')#pobieram z formularza wartość 'waluta'
       ilość =request.form['ilość']#pobieram z formularza wartość 'ilość'
       get_rate('data.csv', 'waluta')#odpalam funkcje wybierającą z pliku z api wybraną w formularzu walutę
       wynik=float(ilość)*float(waluta)#przypisuję do zmiennej 'wynik' iloczyn floatów z 'waluty' i 'ilości'
       return render_template('form.html', wynik=wynik)#zwracam formularz z wartością iloczynu w miejscu 'wynik'; nie rozumiem czemu muszę napisać wynik=wynik
'''
@app.route('/', methods=['GET', 'POST']) 
def currency():#nie wiem czy prawidłowo rozumiem tą funkcję:
   if request.method == 'GET': #jeśli zapytanie request to get
       return render_template ("form.html")#to zwraca formularz na stronie
   elif request.method == 'POST':#jeśli zapytanie request to post to
       data=request.form #która wersja zapisu pobierania danych jest poprawna z get czy request.form?
       waluta=data.get('waluta')#pobieram z formularza wartość 'waluta'
       ilość =data.get('ilość')#pobieram z formularza wartość 'ilość'
       get_rate('data.csv', 'waluta')#odpalam funkcje wybierającą z pliku z api wybraną w formularzu walutę
       wynik=float(ilość)*float(waluta)#przypisuję do zmiennej 'wynik' iloczyn floatów z 'waluty' i 'ilości'
       return render_template('form.html', wynik=wynik)#zwracam formularz z wartością iloczynu w miejscu 'wynik'; nie rozumiem czemu muszę napisać wynik=wynik
'''

if __name__ == "__main__":
    app.run(debug=True)