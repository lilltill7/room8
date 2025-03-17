from flask import Flask, render_template
from flask import Flask, render_template, request
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__, static_folder='static')


@app.route("/")
def home():
    return render_template("home.html")

# Route for "find a room8!" page.
@app.route("/find_room8", methods=["GET", "POST"])
def find_room8():
    if request.method == "POST":
        # Demo: we don't process form data yet.
        pass
    return render_template("find_room8.html")

@app.route('/static/images/<filename>')
def get_image(filename):
    return send_from_directory('static/images', filename)

# Route for the Mission page.
@app.route("/mission")
def mission():
    return render_template("mission.html")

# Route for the How It Works page.
@app.route("/how_it_works")
def how_it_works():
    return render_template("how_it_works.html")

# New route for the Login page.
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Here you would normally process the login details.
        pass
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True, port=3000)