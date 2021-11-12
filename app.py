from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    first_name = "Shohan"
    tittle = "This is cool thing"
    stuff = "this is <strong>Bold</strong> "
    pizza = ['Pepparoni','cheese','moyda',41]
    return render_template("index.html",
    first_name = first_name,
    stuff = stuff,
    tittle = tittle,
    pizza =pizza
    
    )

@app.route("/user/<name>")
def user(name):
    return render_template("user.html",user_name = name)
# Create custom Error pages
#invalid URL

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html") ,404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html") ,500
