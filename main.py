from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Clave de API desde variable de entorno
openai.api_key = os.getenv("Kairo-01")

@app.route("/", methods=["GET"])
def home():
    return "Hola, soy Kairo-01"

@app.route("/kairo", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("mensaje", "")

    if not prompt:
        return jsonify({"error": "Mensaje vacío"}), 400

    # Hacer la llamada a la API de OpenAI
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        mensaje = respuesta.choices[0].message["content"]
        return jsonify({"respuesta": mensaje})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
