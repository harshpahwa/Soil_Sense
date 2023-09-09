from flask import Flask, render_template, request
from flask import  redirect, url_for

import werkzeug

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


#brain tumor
@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__=="__main__":
    app.run(debug=True,port=8000)