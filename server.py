from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<string:color>/<int:x>')
def play(color = "blue", x = 1):
    return render_template("index.html", color = color, x = x)


if __name__ =="__main__":
    app.run(debug=True)