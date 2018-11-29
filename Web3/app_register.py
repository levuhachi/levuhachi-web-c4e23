from flask import Flask, render_template, request
import mlab
from register import Register
from gmail import GMail, Message

mlab.connect()
app = Flask(__name__)

@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method == "GET":
        # User requests Form 
        return render_template("register.html")
    elif request.method == "POST":
        form = request.form
        e = form["email"]  
        un = form["username"]
        pw = form["password"]
        exist_user = Register.objects(username = un).first()
        if exist_user != None: #Found exisitng user
            return "Failed"
        else:
            r = Register(username = un, password = pw, email = e)
            r.save()

            # gmail = GMail("anonymus.hchi@gmail.com","hachi123456")
            # template = "Welcome {{name}} to the website"
            # name = un
            # content = template.replace("{{name}}",name)
            # message = Message("Welcome Email", to= e, text=content)
            # gmail.send(message)

            return "Bravo!!!"

if __name__ == "__main__":
    app.run(debug=True)
