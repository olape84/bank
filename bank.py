import csv

with open ('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
@app.route('/', methods=['GET', 'POST'])
def currency():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return amount * bid

if __name__ == "__main__":
    app.run(debug=True)