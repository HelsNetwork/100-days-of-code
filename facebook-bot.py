import random
from flask import Flask, request
from pymessenger.bot import Bot  
  

app = Flask(__name__)
ACCESS_TOKEN = 'YOUR ACCESS TOKEN'
VERIFY_TOKEN = 'YOUR VERIFY TOKEN'
bot = Bot(ACCESS_TOKEN)

@app.route("/", methods=['GET', 'POST'])
def retrieve_messages():
	if(request.method == 'GET'):
		token = request.args.get("hub.verify_token")
		return verify_token(token)
	elif(request.method == 'POST'):
		output = request.get_json()
		for event in output['entry']:
			messaging = event['messaging']
			for message in messaging:
				if message.get('message'):
					recipient_id = message['sender']['id']
					if message['message'].get('text'):
						response_sent_text = generate_message ()
						message_send(recipient_id, response_sent_text)
					if message['message'].get('attachments'):	
						response_sent_nontext = generate_message()
						message_send(recipient_id, response_sent_nontext)
	return "Processed"

  

def verify_token(token):
	if token == VERIFY_TOKEN:
		return request.args.get("hub.challenge")
	return 'Verification token is invalid'

  

def generate_message():
    response_u = ["YOUR MESSAGE"]
    return random.choice(response_u)

  

def message_send(recipient_id, response):
	bot.send_text_message(recipient_id, response)
	return "success"

  
  

if __name__ == "__main__":
	app.run(host='0.0.0.0', port= )
