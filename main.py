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
script_pages =[
"gui.html",
"dimension.html",
"player.html",
"server.html",
"client.html",
"gfx.html",
"filesystem.html",
"client_settings.html",
"attributes.html",
"attribute.html",
"biome.html",
"block.html",
"effects.html",
"font.html",
"file.html",
"inventory.html",
"item.html",
"module.html",
"visual_module.html",
"script_module.html",
"setting.html",
"color_setting.html",
"attributeid.html",
"effectid.html",
"flags.html",
"setting_type.html",
"global.html"
]
#@app.route("/scripting/")
def scrpting_main():
    return redirect (url_for("scripting_main"))
@app.route("/scripting")
def scripting_main():
    return render_template("scripting/main.html")
@app.route("/scripting/<page>")
def scripting_page(page):
    for i in script_pages:
        if i[:-5] == page:
            return render_template("scripting/"+i)
    else: abort(404)
@app.route("/<page>")########################
def amongus(page):
    if page in script_pages:
        return redirect(url_for("scripting_page", page = page[:-5]))
    else: abort(404)
app.register_error_handler(500, dumbservererror)
app.register_error_handler(404,pageunfound)
app.run()
