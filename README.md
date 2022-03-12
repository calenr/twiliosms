# twilio-msg

## Installation
```
pip install git+https://github.com/calenr/twilio-msg
```

## Authentication
First, export these variables to your environment
```
export TWILIO_ACCOUNT_SID=your_id
export TWILIO_API_KEY=your_key
export TWILIO_API_KEY_SECRET=your_secret
```

## Usage
### Command Line
```
send_msg.py -h
```
### Python
```
from twilio_sms.send_sms import send_message
send_message(sender='+12223334444',
             recvr ='+12223334445',
             body='Message Body')
```
