from flask import Flask,render_template

app = Flask(__name__)

@app.route("/users/<username>")
def profile(username):
    users = { 
        "huy": { 
            "name" : "Nguyen Quang Huy", 
            "age" : 29
            },
        "tuananh": {
                "name" : "Huynh Tuan Anh",
                "age" : 22
            }
    }
    if username in users:
        name = username
        profile = users[username]
    else:
        return "User Not Found"

    return render_template("profile.html",name = name, profile = profile)
if __name__ == "__main__":
    app.run(debug=True) 