from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():  
    return "It Works!!"

if __name__ == "__main__":
    app.run()
