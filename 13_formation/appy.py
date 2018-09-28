from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form_example():
    #print(app);
    return render_template("form_example.html")

@app.route("/auth")
def auth():
    #print(request)
    #print(request.headers)
    #print(request.method)
    #print(request.args['username'])
    #print(request.form)
    return render_template("greet.html", user = request.args['username'], method = request.method)

if __name__ == "__main__":
	app.debug = True
	app.run()
