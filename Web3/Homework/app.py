from flask import Flask, render_template, request
import mlab
from ex2 import Bike

mlab.connect()
app = Flask(__name__)

@app.route("/new_bike", methods = ["GET","POST"])
def new_bike():
    if request.method == "GET":
        return render_template("ex1.html")
    else:
        form = request.form
        model = form["model"]
        fee = form["daily_fee"]
        img = form["image"]
        year = form["year"]
# Ex3:
        d = {
            "Model": model,
            "Daily Fee (VND)": fee,
            "Image": img,
            "Year": year,
        }
        print(d)
# Ex4
        rental = Bike(model=model, fee = fee, image = img, year = year)
        rental.save()
        return ("We will check it out as soon as possible")

if __name__ == "__main__":
    app.run(debug=True)