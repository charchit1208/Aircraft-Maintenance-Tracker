from flask import Flask, render_template,request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-aircraft',methods=['GET','POST'])
def add_aircraft():
    if request.method == 'POST':
        aircraft_id = request.form['aircraft_id']
        model = request.form['model']
        manufacturer = request.form['manufacturer']
        year = request.form['year']
        status = request.form['status']
        print("Form Submitted")

        # Just print for now (can later save to DB )
        print(f"Received: {aircraft_id},{model},{manufacturer},{year},{status}")

        return redirect(url_for('home'))
    return render_template('add_aircraft.html')


if __name__ == '__main__':
    app.run(debug=True)
