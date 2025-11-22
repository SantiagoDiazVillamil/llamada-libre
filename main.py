# from flask import Flask, request
# from twilio.rest import Client

# # Twilio credentials (set these as environment variables in real use!)
# account_sid = "ACe7c1a99d9eb4462db147"
# auth_token = "de92cadbf44ca7cba6632"
# twilio_number = "+12409988529"   # Your Twilio phone number
# to_number = "+573147257733"     # The number you want to call

# client = Client(account_sid, auth_token)
# app = Flask(__name__)

# @app.route("/voice_", methods=["POST"])
# def voice():
#     # TwiML asking for speech input
#     twiml = """
#     <Response>
#         <Gather input="speech" language="es-ES" action="/gather">
#             <Say voice="Google.es-ES-Chirp3-HD-Puck">
#                 Por favor, dígame qué plato desea ordenar.
#             </Say>
#         </Gather>
#         <Say>No se recibió ninguna respuesta.</Say>
#     </Response>
#     """
#     return twiml

# @app.route("/gather_", methods=["POST"])
# def gather():
#     # Twilio sends the transcription here
#     speech_result = request.form.get("SpeechResult", "")
#     print(f"Cliente dijo: {speech_result}")
#     return f"<Response><Say>Gracias, hemos registrado su pedido: {speech_result}</Say></Response>"


# @app.route("/health_", methods=["GET"])
# def health():
#     return {"status": "ok", "message": "Cloud Run service is working"}



import os
from flask import Flask

app = Flask(__name__)

@app.route("/health_", methods=["GET"])
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
