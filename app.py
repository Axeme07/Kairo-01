from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, soy Kairo-01!"

if __name__ == "__main__":
    app.run(debug=True)
  
