from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)

openai.api_key = 'sk-proj-L7JJk8vI22rNy02hs6S3T3BlbkFJaN4cmGJ1iJEib91SoQe1'

def obter_resposta(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
    msg = resp.message()

    resposta_chatgpt = obter_resposta(incoming_msg)
    msg.body(resposta_chatgpt)

    return str(resp)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
