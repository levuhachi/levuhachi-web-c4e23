from flask import Flask,render_template

# __name__ show the "app" where it is to load
app = Flask(__name__)

#function binding:
@app.route("/")  # "/" : home page --> If user accesses to homepage, then the following function will run
def home(): 
    return "Hello Flask"

@app.route("/c4e")
def c4e():
    return "Hello C4E !^_^"

@app.route("/me")
def me():
    return "My name is Chi :)"

@app.route("/hi/<name>")
def greetings(name):
    return "Hi " + name

# @app.route("/add/<a>/<b>")
# def add(a,b):
#     s = int(a) + int(b)
#     return str(s)

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    s = a + b
    return str(s)  

@app.route("/posts/<int:index><int:j>")
def posts(index,j):
    titles = [
        "What heavy rain!",
        "I need to bring the umbrella",
        ":D",
    ]
    contents = [
        "It has been raining for 3 days",
        "My umbrella does not work",
    ]
    t = titles[index]
    c = contents[j]
    return render_template("post.html", title = t, content= c)

@app.route("/movie")
def movie():
    return render_template("movie.html", name = "Deadpool", image="https://upload.wikimedia.org/wikipedia/en/thumb/2/23/Deadpool_%282016_poster%29.png/220px-Deadpool_%282016_poster%29.png")    

@app.route("/movies")
def movies():
    # movie_titles = ["Deadpool","Superman","Batman"]
    # return render_template("moviess.html", titles = movie_titles)
    movie_lists = [
        {
            "title":"Deadpool",
            "image":"https://upload.wikimedia.org/wikipedia/en/thumb/2/23/Deadpool_%282016_poster%29.png/220px-Deadpool_%282016_poster%29.png"
        },
        {
            "title":"Batman",
            "image":"https://upload.wikimedia.org/wikipedia/en/8/87/Batman_DC_Comics.png"
        },
        {
            "title":"Superman",
            "image":"https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/SupermanRoss.png/250px-SupermanRoss.png"
        }
    ]

    return render_template("moviess.html",movies = movie_lists )

#deploy to server
if __name__ == "__main__":
    app.run(debug=True) 
## http://127.0.0.1 --> local host,loop back


