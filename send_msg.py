#!/usr/bin/env python

# Download the helper library from https://www.twilio.com/docs/python/install
import os
import sys
import argparse as ap
from twilio.rest import Client


def parse_args(*args):
    parser = ap.ArgumentParser()
    parser.add_argument('--sender',type=str)
    parser.add_argument('--recvr',type=str)
    parser.add_argument('--body',type=str,default="This message send via python script")
    args = parser.parse_args(*args)
    return args

def send_message(*args):
    args = parse_args(*args)
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    api_key = os.environ['TWILIO_API_KEY']
    api_secret = os.environ['TWILIO_API_KEY_SECRET']
    client = Client(api_key, api_secret, account_sid)

    '''
    message = client.messages.create(
                                from_=args.sender,
                                body='Hi there',
                                to=args.recvr
                            )
    print(message.sid)
    '''


if __name__ == "__main__":
    send_message(sys.argv[1:])
