from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "temp"

@app.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("test.html")


if __name__ == "__main__":
    app.debug = True
    app.run()