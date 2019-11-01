from flask import Flask, render_template  

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("start.html")
    
@app.route("/play")
def play():
    return render_template("play.html")

@app.route("/results")
def results():
    return render_template("results.html")
    
if __name__ == "__main__":
    app.run(debug=True)