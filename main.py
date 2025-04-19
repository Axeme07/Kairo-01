from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Clave de API desde variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def home():
    return "Hola, soy Kairo-01"

@app.route("/kairo", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("mensaje", "")

    if not prompt:
        return jsonify({"error": "Mensaje vacío"}), 400

    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    mensaje = respuesta.choices[0].message["content"]
    return jsonify({"respuesta": mensaje})
