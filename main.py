from flask import *

app = Flask(__name__)
class Error(Exception):
    pass
#main html
@app.route("/")
def main():
    return render_template("index.html")
@app.route("/index.html")
def redirect_to_main():
    return redirect(url_for("main"))
@app.route("/favicon.ico")
def favicon():
    return send_from_directory("templates","favicon.ico")
@app.route("/style.css")
def style():
    
    return send_from_directory("templates","style.css")
@app.route("/assets/logo.png")
def logo():
    return send_from_directory("templates/assets","logo.png")
@app.route("/MobileBlock.js")
def block():
    return send_from_directory("templates","MobileBlock.js")
def pageunfound(e):
    return render_template("404.html")
def dumbservererror(e):
    return render_template("500.html")
@app.route("/500")
def fivehundred():
    try:
        raise(Error("Why would anyone visit this path?"))
    except Error as e:
        print(e)
        abort(500)
@app.route("/license")
def license():
    return render_template("license.html")
@app.route("/license.html")
def licence():
    return redirect (url_for("license"))
#scripting
@app.route("/scripting")
def scripting_main():
    return render_template("scripting/main.html")


app.register_error_handler(500, dumbservererror)
app.register_error_handler(404,pageunfound)
app.run()
