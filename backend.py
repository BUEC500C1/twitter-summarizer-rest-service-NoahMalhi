from flask import Flask, escape, request, render_template, redirect

app = Flask(__name__)


if (__name__ == "__main__"):
    app.run(
        host="127.0.0.1",
        port=5000
)

@app.route('/')
def hello():
    return render_template("main.html")
    #name = request.args.get("name", "World")
    #return f'Hello, {escape(name)}!'

#redirect route to data page after sign in
@app.route("/callback")
def callback():
    return render_template("data_page.html")
