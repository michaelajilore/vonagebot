import vonage
from time import sleep
import tkinter as tk

# Vonage API credentials
api_key = 'db6a10ce'
api_secret = 'dcjCnMt6qsvHugaN'
control = 0

# Initialize Vonage client
client = vonage.Client(key=api_key, secret=api_secret)
sms = vonage.Sms(client)

# Send SMS message
response1 = sms.send_message({
    'from': '12088498549',
    'to': '18327076472',
    'text': 'hello i am a text bot programmed by Michael Ajilore ive been programmed to keep texting you yelenas face until you send michael a text '
})
if response1['messages'][0]['status'] == '0':
    print('Message sent successfully.')
else:
    print(f'Error: {response1["messages"][0]["error-text"]}')

sleep(5)



while True:
    response = sms.send_message({
    'from': '12088498549',
    'to': '18327076472',
    'text': 'https://i.pinimg.com/736x/8d/a3/58/8da358d15d6f81ad26edca55f53d26c2.jpg '
})

    if response['messages'][0]['status'] == '0':
        print('Message sent successfully.')
    else:
        print(f'Error: {response["messages"][0]["error-text"]}')
    sleep(10)





