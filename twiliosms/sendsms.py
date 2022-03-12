#!/usr/bin/env python

# Download the helper library from https://www.twilio.com/docs/python/install
import os
import sys
import argparse as ap
from twilio.rest import Client


def parse_args(*args):
    parser = ap.ArgumentParser()
    parser.add_argument('--sender',type=str, required=True,
                        help="The phone number to send SMS from. Must be an active number in your twilio account. Must be in format +12223334444")
    parser.add_argument('--recvr',type=str, required=True,
                        help="The phone number to send SMS to. Must be in format +12223334444")
    parser.add_argument('--body',type=str,default="This message send via python script",
                        help="The body of the text message")
    args = parser.parse_args(*args)
    return args

def send_message(sender, recvr, body="This is an sms from python via twilio"):
    try:
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        api_key = os.environ['TWILIO_API_KEY']
        api_secret = os.environ['TWILIO_API_KEY_SECRET']
        client = Client(api_key, api_secret, account_sid)

        message = client.messages.create(
                                    from_=sender,
                                    body=body,
                                    to=recvr
                                    )
    except Exception as e:
        print("Error: Could not send message via twilio")
        print(e)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    send_message(args.sender, args.recvr, args.body)
