from flask import Flask, render_template
app = Flask(_name_)

@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)

app.run()
