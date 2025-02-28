"""Script Starter Kit"""
import argparse
import json
import os

from aiohttp import web

from aries_staticagent import (
    StaticConnection,
    crypto,
    utils,
    Message
)


def config():
    """ Get config """
    def environ_or_required(key):
        if os.environ.get(key):
            return {'default': os.environ.get(key)}
        return {'required': True}

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--replace-keys',
        action='store_true',
        dest='replace'
    )
    args = parser.parse_args()
    return args


def create_or_recall_keys(replace: bool = False):
    """Generate keys and save to .keys file."""
    if not os.path.exists('.keys') or replace:
        # Create keypair and write to file
        my_vk, my_sk = crypto.create_keypair()
        did = crypto.bytes_to_b58(my_vk[:16])

        print('DID:', did)
        print('VK:', crypto.bytes_to_b58(my_vk))
        their_vk = input('Their VK: ')
        endpoint = input('Their Endpoint: ')

        with open('.keys', 'w+') as key_file:
            json.dump({
                'did': did,
                'my_vk': crypto.bytes_to_b58(my_vk),
                'my_sk': crypto.bytes_to_b58(my_sk),
                'their_vk': their_vk,
                'endpoint': endpoint
            }, key_file)
    else:
        with open('.keys', 'r') as key_file:
            info = json.load(key_file)
            did = info['did']
            my_vk = info['my_vk']
            my_sk = info['my_sk']
            their_vk = info['their_vk']
            endpoint = info['endpoint']

    return did, my_vk, my_sk, their_vk, endpoint


class Session(object):
    def __init__(self, connection):
        self.connection = connection

    def ping(self):
        type_did = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/trust_ping/1.0/ping"
        self._send({
            "@type": type_did,
            "response_requested": True
        })

    def get_connections(self):
        type_did = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/admin-connections/1.0/connection-get-list"
        self._send({
          "@type": type_did,
          "~transport": {
            "return_route": "all"
          }
        })

    def get_credential_definitions(self):
        type_did = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/" + \
            "admin-credential-definitions/1.0/credential-definition-get-list"
        return self._send({
            "@type": type_did,
            "~transport": {
              "return_route": "all"
            }
        })

    def _send(self, message_body):
        message = Message(message_body)
        print('Sending message:', message.pretty_print())
        reply = self.connection.send_and_await_reply(
            message,
            return_route='all',
            timeout=5
        )
        print('Response:', reply.pretty_print())
        return reply


def main():
    """Main."""
    args = config()
    _did, my_vk, my_sk, their_vk, endpoint = create_or_recall_keys(args.replace)

    conn = StaticConnection(my_vk, my_sk, their_vk, endpoint)
    session = Session(conn)
    session.ping()
    session.get_connections()
    session.get_credential_definitions()


if __name__ == '__main__':
    main()
