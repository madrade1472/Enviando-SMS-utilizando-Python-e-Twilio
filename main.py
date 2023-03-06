from twilio.rest import Client

import keys


client = Client(keys.account_sid, keys.auth_token)
message = client.messages.create(
    
    body="OLÀ MEU NOME È FULANO",
    from_=keys.twilio_number,
    to=keys.target_number
    
    
    
)

print(message.body)