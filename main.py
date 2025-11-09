from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
from vertexai.preview.generative_models import GenerativeModel
import vertexai
import os
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Configura Gemini
vertexai.init(project="portafolio-data", location="us-central1")
gemini_model = GenerativeModel("gemini-2.0-flash-lite-001")

@app.route("/voice", methods=["POST"])
def handle_voice():
    user_input = request.form.get("SpeechResult", "")
    print(f"User said: {user_input}")

    # Genera respuesta con Gemini
    if user_input:
        gemini_response = gemini_model.generate_content(user_input)
        reply = gemini_response.text
    else:
        reply = "I didn't catch that. Could you repeat?"

    # Responde con voz
    response = VoiceResponse()
    response.say(reply, language="en-US")
    response.redirect("/voice")  # Mantiene el ciclo conversacional

    return Response(str(response), mimetype="text/xml")

@app.route("/health", methods=["GET"])
def health_check():
    try:
        prueba_texto=gemini_model.generate_content('Say Hello!')
        return {'status':'ok','gemini_response':prueba_texto.text}
    except Exception as e:
        return {'status':'Error','msg':str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)