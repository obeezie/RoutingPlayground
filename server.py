from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<string:color>/<int:x>')
def play(color, x):
    return render_template("index.html", color = color, x = x)


if __name__ =="__main__":
    app.run(debug=True)