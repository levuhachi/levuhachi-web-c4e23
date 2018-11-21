from flask import Flask,render_template

app = Flask(__name__)

@app.route('/bmi/<int:h0>/<int:m>')
def bmi(h0,m):
    h = h0 / 100
    bmi =  round(m / (h*h))
    if bmi < 16:
        c = "You are Severely underweight"
    elif 16 <= bmi < 18.5:
        c = "You are Underweight"
    elif 18.5 <= bmi <25:
        c = "You are Normal"
    elif 25 <= bmi <30:
        c = "You are Overweight"
    else:
        c = "You are Obese"
    return render_template("bmi.html",bmi = bmi, condition = c)

if __name__ == "__main__":
    app.run(debug=True) 
