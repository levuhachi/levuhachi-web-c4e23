from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form:
        weight = int(request.form.get('weight'))
        height = int(request.form.get('height'))
        bmi = round((weight / ((height / 100) ** 2)), 2)
        if bmi < 16:
            return render_template("bmi_calc.html", bmi=bmi, condition = "You are severly underweight")
        elif 16 <= bmi < 18.5:
            return render_template("bmi_calc.html", bmi=bmi, condition =  "You are Underweight")
        elif 18.5 <= bmi <25:
            return render_template("bmi_calc.html", bmi=bmi, condition =  "You are Normal")
        elif 25 <= bmi <30:
            return render_template("bmi_calc.html", bmi=bmi, condition =  "You are Overweight")
        else:
            return render_template("bmi_calc.html", bmi=bmi, condition = "You are Obese")
    return render_template("bmi_calc.html", bmi=bmi)

if __name__ == '__main__':
    app.run()