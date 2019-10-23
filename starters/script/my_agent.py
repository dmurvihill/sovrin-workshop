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

def noisy_send_and_await_reply(output, conn, msg):
    """Log messages sent as they are sent."""
    if isinstance(msg, dict):
        msg = Message(msg)
    print(output, msg.pretty_print())
    reply = conn.send_and_await_reply(msg, return_route='all', timeout=5)
    print('Response:', reply.pretty_print())
    return reply


def main():
    """Main."""
    args = config()
    _did, my_vk, my_sk, their_vk, endpoint = create_or_recall_keys(args.replace)

    conn = StaticConnection(my_vk, my_sk, their_vk, endpoint)

    noisy_send_and_await_reply(
        'Pinging connection:',
        conn,
        {
            "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/trust_ping/1.0/ping",
            "response_requested": True
        }
    )

    connections = noisy_send_and_await_reply(
        'Fetching connections:',
        conn,
        {
            "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/admin-connections/1.0/connection-get-list",
        }
    )

    holder_connection = next(filter(
        lambda connection: connection['their_label'] == 'Holder',
        connections['results']
    ))
    print('Found holder:', holder_connection)

    cred_def_id = input('Credential Definition ID: ')

    cred_def_info = noisy_send_and_await_reply(
        'Fetching Credential Definition:',
        conn,
        {
            "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/admin-credential-definitions/1.0/credential-definition-get",
            'cred_def_id': cred_def_id
        }
    )

    attributes = []
    for attribute in cred_def_info['attributes']:
        attributes.append({
            'name': attribute,
            'value': input(attribute + ': ')
        })

    print('Issuing credential with attributes:', attributes)
    noisy_send_and_await_reply(
        'Triggering credential send:',
        conn,
        {
            "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/admin-issuer/1.0/send-credential",
            "comment": "testing issuance of credential",
            "credential_definition_id": cred_def_id,
            "connection_id": holder_connection['connection_id'],
            "credential_proposal": {
                "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/issue-credential/1.0/credential-preview",
                'attributes': attributes
            }
        }
    )


if __name__ == '__main__':
    main()
