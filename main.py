from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    variable = "abc"
    return render_template("index1.html", content=variable)

if __name__ == "__main__":
    app.run(debug=True)