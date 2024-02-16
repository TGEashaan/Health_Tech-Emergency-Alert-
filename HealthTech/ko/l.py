from twilio.rest import Client 
account_sid = 'ACfb2b8474d7c44ff3bedb84a051dd7064'
auth_token = 'be9d82aa6cc413512cb7fb35d7dd1cad'
Client = Client(account_sid,auth_token)
#+917416509659
to_number = '+917416509659'
from_number = '+12518424085'
call = Client.calls.create(
                        twiml='<Response><Say>Emergency , Patient : Srikar , Age : 22 , Health condition : Critical , Location : road number 3 </Say></Response>',
                        to=to_number,
                        from_=from_number
)
print(call.sid)
message = Client.messages.create(
    to="+917416509659",
    from_="12518424085",
    body="Patient : Srikar , Age : 22 , Health condition : Critical , Location : road number 3")

print(message.sid)