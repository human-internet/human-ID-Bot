from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success_bot():
    return render_template("success.html")

@app.route("/failure", methods=["POST"])
def failure_bot(): 
    return  render_template("failure.html")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

if __name__ == "__main__":
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=22)
    app.run(host='18.225.5.208', port=5000)

