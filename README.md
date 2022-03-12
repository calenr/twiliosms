# twiliosms
Uses twilio to send a message to your cell phone using Python

## Installation
```
pip install git+https://github.com/calenr/twiliosms
```
## Setup Twilio Account
If you haven't already setup a twilio account, then do so now
1. Create an account: 
   - https://www.twilio.com/try-twilio
2. Add a virtual phone number: 
   - Docs: https://www.twilio.com/docs/glossary/what-virtual-phone-number
   - Console: https://www.twilio.com/console/phone-numbers
3. Create an API key: 
   - Docs: https://www.twilio.com/docs/iam/keys/api-key
   - Console: https://www.twilio.com/console/runtime/api-keys

## Authentication
Export these variables to your environment.

Bash:
```
export TWILIO_ACCOUNT_SID=your_id
export TWILIO_API_KEY=your_key
export TWILIO_API_KEY_SECRET=your_secret
```

Python:
```
os.environ['TWILIO_ACCOUNT_SID'] = "your_id"
os.environ['TWILIO_API_KEY'] = "your_key"
os.environ['TWILIO_API_KEY_SECRET'] = "your_secret"
```

## Usage
### Command Line
```
send_msg.py -h
```
### Python
```
from twiliosms.sendsms import send_message
send_message(sender='+12223334444',
             recvr ='+12223334445',
             body='Message Body')
```
