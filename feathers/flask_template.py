from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('index.html', message="Bienvenue dans PhoenixPy !")

if __name__ == "__main__":
    app.run(debug=True)