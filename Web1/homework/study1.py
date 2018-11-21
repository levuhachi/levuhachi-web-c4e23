from flask import Flask, render_template

app = Flask(__name__)

@app.route("/about-me")
def about_chi():
    intro = """
        Name : Le Vu Ha Chi </br>
        Age: 20 </br>
        D.O.B: 4/9/1998 </br>
        Job: Student </br>
        Major: Accounting"""
    return intro

if __name__ == "__main__":
    app.run(debug=True) 
